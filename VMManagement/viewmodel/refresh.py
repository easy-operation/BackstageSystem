from VMManagement import models

def refresh():
    list = models.ServerInfo.objects.all();
    for obj in list;