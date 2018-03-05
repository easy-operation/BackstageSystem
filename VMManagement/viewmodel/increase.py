import gevent

from VMManagement import models
from django import forms


class ContactForm(forms.Form):
    host = forms.CharField(max_length=50, label='主机IP')
    password = forms.CharField(max_length=50, label='主机密码')


def increase_vm(request):
    print("--------------------")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            host = form.cleaned_data['host']
            password = form.cleaned_data['password']
            obj = models.ServerInfo(ip=host, password=password)
            try:
                obj.save()
                return 0
            except Exception as ex:
                print("\tError %s\n" % ex)
                return ex
    else:
        form = ContactForm()  # 获得表单对象
