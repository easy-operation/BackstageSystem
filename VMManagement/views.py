# -*- coding: utf-8 -*-
from VMManagement.viewmodel.query import queryAll
from VMManagement.viewmodel.refresh import refresh
from django.http import HttpResponse
from VMManagement import  models


def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")


def all(request):
    data = queryAll()
    print(data)
    return HttpResponse(data)


def increase_server(request):

    data = queryAll()
    print(data)
    return HttpResponse(data)


def refresh_view(request):
    refresh()
    data = queryAll()
    return HttpResponse(data)

