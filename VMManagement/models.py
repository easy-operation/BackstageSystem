# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.db import models


# Create your models here.


# 服务器信息类
class ServerInfo(models.Model):
    ip = models.GenericIPAddressField(unique=True)  # 服务器IP
    password = models.CharField(max_length=15)  # 服务器root密码
    # hostname = models.CharField(max_length=50, blank=True, null=True, unique=True)  # 服务器主机名
    hostname = models.CharField(max_length=50, blank=True, null=True)  # 服务器主机名
    cpu_thread = models.IntegerField(blank=True, null=True)  # cpu线程数
    description = models.CharField(max_length=15, blank=True, null=True)  # 用途描述
    system_version = models.CharField(max_length=60, blank=True, null=True)  # 系统版本
    disk = models.CharField(max_length=30, blank=True, null=True)  # 磁盘信息
    total_memory = models.IntegerField(blank=True, null=True)  # 总内存信息
    free_memory = models.IntegerField(blank=True, null=True)  # 已用内存信息
    # apps = models.CharField(max_length=30, blank=True, null=True)  # 运行的app
    status = models.IntegerField(blank=True, null=True, default=1)  # 服务器状态 正常为0 不可达为1

    def __str__(self):
        return self.ip


class ServerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInfo
        fields = ('ip', 'password', 'hostname', 'cpu_thread', 'description',
                  'system_version', 'disk', 'total_memory', 'free_memory', 'status')

