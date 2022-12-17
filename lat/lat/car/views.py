from django import http
from django.shortcuts import render


def car_now(request):
    return http.HttpResponse('It works')


def create_new(request):
    return render(request, 'index.html')


def get_value(request, *args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
    return http.HttpResponse('new style')