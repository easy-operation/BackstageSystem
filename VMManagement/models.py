from django.db import models

# Create your models here.


# 服务器信息类
class ServerInfo(models.Model):
    ip = models.GenericIPAddressField(unique=True)  # 服务器IP
    password = models.CharField(max_length=15)  # 服务器root密码
    hostname = models.CharField(max_length=15, blank=True, null=True, unique=True)  # 服务器主机名
    cpu_thread = models.IntegerField(blank=True, null=True)  # cpu线程数
    description = models.CharField(max_length=15, blank=True, null=True)  # 用途描述
    system_version = models.CharField(max_length=30, blank=True, null=True)  # 系统版本
    disk = models.CharField(max_length=30, blank=True, null=True)  # 磁盘信息
    memory = models.CharField(max_length=30, blank=True, null=True)  # 内存信息
    # apps = models.CharField(max_length=30, blank=True, null=True)  # 运行的app
    status = models.IntegerField(blank=True, null=True)  # 服务器状态 正常为0 不可达为1

    def __str__(self):
        return self.ip
