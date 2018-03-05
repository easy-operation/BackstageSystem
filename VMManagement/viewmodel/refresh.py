import gevent as gevent

from VMManagement import models
from subprocess import Popen, PIPE
import re
import os, sys
import paramiko
import gevent


def refresh():
    # listA = models.ServerInfo.objects.all()
    # for obj in listA:
    #     # print(obj.ip + obj.password)
    #     status = health(obj.ip, obj.password)
    #     if status is None:  # 非空判断
    #         obj.status = 1
    #         obj.save()  # 赋值保存
    #         break
    #         # print(status)
    #     elif status is not None and status != 0:
    #         obj.status = 0
    #         obj.save()  # 赋值保存
    #         # print(status)
    #     hostname = execute(obj.ip, obj.password, "hostname")
    #     sys_vertion = execute(obj.ip, obj.password, "cat /etc/redhat-release")
    #     memory = execute(obj.ip, obj.password, "free -h|awk '{print $2}'|sed -n 2p") + '/' \
    #      + execute(obj.ip, obj.password, "free -h|awk '{print $3}'|sed -n 2p")
    #     if hostname is not None:  # 非空判断
    #         obj.hostname = hostname
    #         obj.save()  # 赋值保存
    #         # print(hostname)
    #     if sys_vertion is not None:  # 非空判断
    #         obj.system_version = sys_vertion
    #         obj.save()  # 赋值保存
    #         # print(sys_vertion)
    #     if memory is not None:   # 非空判断
    #         obj.memory = memory
    #         obj.save()  # 赋值保存
    #         # print(memory)
    listA = models.ServerInfo.objects.all()
    threads = []
    for obj in listA:
        threads.append(gevent.spawn(server_info, obj))
    gevent.joinall(threads)


def server_info(obj):
    try:
        obj.status = 1
        obj.save()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(obj.ip, 22, 'root', obj.password, timeout=1)  # 超时时间设置少的话,无法建立会话
        gevent.sleep(0)  # 切换协程
        stdin, stdout, stderr = ssh.exec_command("hostname")
        server_name = stdout.read().decode('utf-8')  # 将 b'example\n' 转化为 'example'
        server_name = ''.join(server_name).strip('\n')  # 去掉\n

        stdin, stdout, stderr = ssh.exec_command("cat /etc/system-release")
        sys_vertion = stdout.read().decode('utf-8')  # 将 b'example\n' 转化为 'example'
        sys_vertion = ''.join(sys_vertion).strip('\n')  # 去掉\n

        stdin, stdout, stderr = ssh.exec_command("free -m|awk '{print $2}'|sed -n 2p")
        total_memory = stdout.read().decode('utf-8')  # 将 b'example\n' 转化为 'example'
        total_memory = ''.join(total_memory).strip('\n')  # 去掉\n

        stdin, stdout, stderr = ssh.exec_command("free -m|awk '{print $3}'|sed -n 2p")
        used_memory = stdout.read().decode('utf-8')  # 将 b'example\n' 转化为 'example'
        used_memory = ''.join(used_memory).strip('\n')  # 去掉\n
        print(server_name + total_memory + '----------' + used_memory)

        # print(obj.ip + '的已用内存为: %d', used_memory)

        obj.hostname = server_name
        obj.system_version = sys_vertion
        obj.total_memory = total_memory
        obj.used_memory = used_memory
        obj.status = 0
        obj.save()
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
    print
    "begin"
    execute()
