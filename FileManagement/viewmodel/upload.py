import paramiko


def uploadFile(file, host, password, username):
    try:
        t = paramiko.Transport((host, 22))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        # 上传文件
        sftp.put("/home/application/user.db", "/data/user/user.db")
        sftp.put()
        t.close()
    except Exception as e:
        print(e)
