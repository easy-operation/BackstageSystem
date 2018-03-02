# Create your views here.
from VMManagement.src.query import queryAll
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")


def all(request):
    data = queryAll()
    print(data)
    return HttpResponse(data)

