# -*- coding:utf-8 -*-
from django.core import serializers

from VMManagement.models import ServerInfo


def queryAll():
    print("中文")
    print(ServerInfo.description)
    servers_info = serializers.serialize("json", ServerInfo.objects.all())
    return servers_info
