from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import Venda
from .forms import VendaForm


class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Permissão Negada!')

        # return super(DashboardView, self).dispatch(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        dct_ = {}
        objs = Venda.objects

        dct_['media'] = objs.media()
        dct_['media_desconto'] = objs.media_descontos()
        dct_['venda_min'] = objs.venda_minima()
        dct_['venda_max'] = objs.venda_maxima()
        dct_['qtd_vendas'] = objs.qtd_vendas()
        dct_['total_vendas'] = objs.total_vendas()
        dct_['media'] = objs.media()
        dct_['num_ped_nfe'] = objs.num_ped_nfe()

        return render(request, 'vendas/dashboard.html', dct_)


class NovoPedido(View):
    def get(self, request):
        data = {}
        data['vendaform'] = VendaForm
        return render(request, 'vendas/novo-pedido.html', data)

    def post(self, request):
        data = {}
        data['numero'] = request.POST['numero']
        data['desconto'] = float("0"+request.POST.get('desconto'))
        data['venda_id'] = request.POST['venda_id']

        if data['venda_id']:
            venda = Venda.objects.get(id=data['venda_id'])
        else:
            venda = Venda.objects.create(numero=data['numero'],
                                         desconto=data['desconto'])

        items = venda.itemdopedido_set.all()
        data['venda_obj'] = venda
        data['items'] = items
        return render(request, 'vendas/novo-pedido.html', data)


class VendaCreateView(CreateView):
    model = Venda
    fields = '__all__'
