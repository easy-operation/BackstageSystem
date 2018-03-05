import gevent as gevent

from VMManagement import models
from subprocess import Popen, PIPE
import os, sys
import paramiko
import gevent


# 刷新主机信息
def refresh():

    listA = models.ServerInfo.objects.all()
    threads = []
    for obj in listA:
        threads.append(gevent.spawn(server_info, obj))
    gevent.joinall(threads)


def server_info(obj):
    try:
        # 初始化主机状态
        obj.status = 1
        obj.save()
        # 建立ssh链接
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(obj.ip, 22, 'root', obj.password, timeout=1)  # 超时时间设置少的话,无法建立会话
        gevent.sleep(0)  # 切换协程
        # 获取hostname
        stdin, stdout, stderr = ssh.exec_command("hostname")
        server_name = stdout.read().decode('utf-8')  # 将 b'example\n' 转化为 'example'
        server_name = ''.join(server_name).strip('\n')  # 去掉\n
        # 获取系统版本
        stdin, stdout, stderr = ssh.exec_command("cat /etc/system-release")
        sys_vertion = stdout.read().decode('utf-8')  # 将 b'example\n' 转化为 'example'
        sys_vertion = ''.join(sys_vertion).strip('\n')  # 去掉\n
        # 获取内存总数
        stdin, stdout, stderr = ssh.exec_command("free -m|awk '{print $2}'|sed -n 2p")
        total_memory = stdout.read().decode('utf-8')  # 将 b'example\n' 转化为 'example'
        total_memory = ''.join(total_memory).strip('\n')  # 去掉\n
        # 获取可用内存
        stdin, stdout, stderr = ssh.exec_command("free -m|awk '{print $3}'|sed -n 2p")
        used_memory = stdout.read().decode('utf-8')  # 将 b'example\n' 转化为 'example'
        used_memory = ''.join(used_memory).strip('\n')  # 去掉\n
        # 赋值
        obj.hostname = server_name
        obj.system_version = sys_vertion
        obj.total_memory = total_memory
        obj.used_memory = used_memory
        obj.status = 0
        # 保存到库
        obj.save()
        # 断开链接
        ssh.close()
    except Exception as ex:
        print("\tError %s\n" % ex)


# 连接远程服务器,执行cmd
# 入参：host主机名（IP）、cmd（执行的shell）
def execute(host, passwd, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, 22, 'root', passwd, timeout=1)
        gevent.sleep(0)  # 切换协程
        stdin, stdout, stderr = ssh.exec_command(cmd)
        re = stdout.read().decode('utf-8')  # 将 b'example\n' 转化为 'example'
        re = ''.join(re).strip('\n')  # 去掉\n
        return re
        ssh.close()
    except Exception as ex:
        print("\tError %s\n" % ex)


if __name__ == '__main__':
    print("self")
    refresh()
