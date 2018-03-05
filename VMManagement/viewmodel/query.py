# -*- coding: utf-8 -*-
from django.core import serializers

from VMManagement.models import ServerInfo


def queryAll():
    print("中文")
    servers_info = serializers.serialize("json", ServerInfo.objects.all(), ensure_ascii=False,)
    print(servers_info)
    return servers_info
