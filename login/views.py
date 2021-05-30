from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models

user_list = []


# Create your views here.

def index(request):
    # return HttpResponse('Hello World!')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        models.UserInfo.objects.create(user=username, pwd=password)

    # 从数据库中读取数据
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})
