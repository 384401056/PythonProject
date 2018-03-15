from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    # 设置session
    # request.session['k1'] = 123
    request.session.setdefault('k2', 456)  # 存在则不设置.

    return HttpResponse('index OK')


def getSession(request):
    """服务器端的session默认是存在数据库中的。"""

    # 获取session
    # print(request.session['k1'])
    print(request.session.keys())
    print(request.session.values())
    print(request.session.items())

    # 查看当前浏览器用户的随机字符串
    print('当前浏览器用户随机字符串:', request.session.session_key)

    # 将所有失效日期小于当前日期的session数据删除。session的默认有效时间是两周.
    # request.session.clear_expired()

    # 检查用户session的随机字符串在数据库中是否存在。
    # print(request.session.exists('96ykjck6ju20b2gs51y8bj0gf1jb525q'))


    return HttpResponse('getSession OK')


def delSession(request):
    del request.session['k1']
    return HttpResponse('delSession OK')
