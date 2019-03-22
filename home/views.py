from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import logout
from django.views.generic import View


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
