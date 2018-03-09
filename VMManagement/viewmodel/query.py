# -*- coding: utf-8 -*-

from VMManagement import models
from VMManagement.viewmodel import serialize


def queryAll():
    data = models.ServerInfo.objects.all().order_by("ip")  # 获取所有数据
    counts = models.ServerInfo.objects.all().count()
    serializer = models.ServerInfoSerializer(data, many=True)
    json = {'data': serializer.data, 'total': counts}
    return serialize.JSONResponse(json)
