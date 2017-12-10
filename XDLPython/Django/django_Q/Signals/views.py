from django.shortcuts import render
from . import models
# Create your views here.

"""Django中的信号"""
def index(request):
    print('before save model')
    models.Signal_User.objects.create(username='gaoyanbin') # 创建数据库数据。
    print('after save model')
    return render(request, 'Signals/index.html')

"""自定义信号"""
def index2(request):
    from Signals import my_signal

    # 触发信号.
    my_signal.send(sender='index2', arg1= 'kkkk', arg2='123')
    return render(request, 'Signals/index2.html')