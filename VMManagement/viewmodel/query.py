# -*- coding: utf-8 -*-
from django.core import serializers

from VMManagement.models import ServerInfo


def queryAll():
    servers_info = serializers.serialize("json", ServerInfo.objects.all(), ensure_ascii=False)
    return servers_info
