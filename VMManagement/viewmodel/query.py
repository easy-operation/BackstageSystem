# -*- coding: utf-8 -*-

from VMManagement import models
from VMManagement.viewmodel import serialize


def queryAll():
    data = models.ServerInfo.objects.all().order_by("ip")
    serializer = models.ServerInfoSerializer(data, many=True)
    print(serializer.data)
    return serialize.JSONResponse(serializer.data)
