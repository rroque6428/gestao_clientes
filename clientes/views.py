from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Person
from .forms import PersonForm


class PersonList(ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['now'] = timezone.now()
        context['ja_acessou'] = self.request.session.get('ja_acessou', False)

        self.request.session['ja_acessou'] = True

        return context


class PersonDetail(DetailView):
    model = Person


class PersonCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Person
    fields = '__all__'
    success_url = reverse_lazy('person_list_cbv')
    permission_required = ('clientes.add_person',)


class PersonUpdate(UpdateView):
    model = Person
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('person_list_cbv')


class PersonDelete(DeleteView):
    model = Person
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('person_list_cbv')


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('Não autorizado')

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})