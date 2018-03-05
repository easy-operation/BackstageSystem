# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path
from VMManagement import views as index

urlpatterns = [
    path('', index.index),
    path('all/', index.all),
    path('refresh/', index.refresh_view),
    path('admin/', admin.site.urls),
]
