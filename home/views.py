import json
import random

from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.views.generic import View, TemplateView


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')


class MyView(View):
    def get(self, request, *args, **kwargs):
        response = render_to_response('home3.html', context=request.COOKIES)
        response.set_cookie('color', 'blue', max_age=1000)
        return response

    def post(self, request, *args, **kwargs):
        return HttpResponse('<h1>Hi</h1>')


class VueJSTestView(TemplateView):
    template_name = 'home/vue-test.html'

    names = ("bob", "dan", "jack", "lizzy", "susan")
    items = []
    for i in range(100):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20, 80),
            "url": "https://example.com",
        })

    extra_context = {
        "items": items,  # Django
        "items_json": json.dumps(items)  # VueJS

    }
