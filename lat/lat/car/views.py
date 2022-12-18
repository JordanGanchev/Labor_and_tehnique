from django import http
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return http.HttpResponse('It works')


def create_new(request):
    return render(request, 'index.html')


def get_view(request, *args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
    return http.HttpResponse('new style')


# def show_cars(request: HttpResponse, *args, **kwargs):
#     body = f'{request.path}, args={args}, kwargs={kwargs}'
#     return HttpResponse(body)

def show_cars(request: HttpResponse, *args, **kwargs):
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.get_port())
    print(request.get_host())
    print(request.headers)

    order_by = request.GET.get('order_by', 'name')
    body = f'path: {request.path}, args={args}, kwargs={kwargs}, order_by: {order_by}'
    return HttpResponse(body)
