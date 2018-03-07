# -*- coding: utf-8 -*-
from django.shortcuts import render

from VMManagement.viewmodel.increase import increase_vm
from VMManagement.viewmodel.query import queryAll
from VMManagement.viewmodel.refresh import refresh
from django.http import HttpResponse
from VMManagement.viewmodel import increase


def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")


def all(request):
    data = queryAll()
    print(data)
    return HttpResponse(data)


def refresh_view(request):
    refresh()
    data = queryAll()
    return HttpResponse(data)


def increase_vm_view(request):
    status = increase_vm(request)
    if status == '0':
        return HttpResponse("成功")
    else:
        return HttpResponse(status)


