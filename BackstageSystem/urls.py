# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path
from VMManagement import views as index

urlpatterns = [
    path('', index.index),
    path('operations/vm/all/', index.all),
    path('refresh/', index.refresh_view),
    path('operations/vm/increase/', index.increase_vm_view),
    path('admin/', admin.site.urls),
]
