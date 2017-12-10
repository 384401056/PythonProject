from django.shortcuts import render, HttpResponse
import json
# Create your views here.

def index(request):

    # print(request.COOKIES['k1'])  # 第一次访问时可能无cookies
    # 1. 获取response对象
    ret = HttpResponse('index ok')

    # 获取签名cookies
    # print(request.get_signed_cookie('k1', None, salt='gaoyanbin'))

    # 设置cookie
    # ret.set_cookie('k1', 123)
    # ret.set_signed_cookie(key='k1', value='abcdefghijklmn', salt='gaoyanbin')
    # 打印cookie

    # 默认设置的cookies是全局的，也就是其它url中也可取得。
    # 添加path后就可以指定哪些url才能得到。
    # ret.set_cookie('k1', 8888)
    ret.set_cookie(
        'kkk999', 123456,
        max_age= 10, # 超时时间。以秒为单位，多少秒后失效。
        expires= 10, # 超时时间。以日期为单位，IE浏览器要设置，目前所有浏览器都支持。这两个只需写一个,Django默认会写上另一个。
        path='/cook1/', # 只有在/cook1/下能获取
        domain=None, # 只有在当前域名下能获取（默认)
        secure=False, # 是否使用https传输。
        httponly=False, # 当为True时，只能http协议传输。无法用javascript抓取。（不是绝对的，底层抓包可以抓到并覆盖。）
    )

    return ret

"""可以获取到kkk999"""
def cook1(request):
    ret_cook = request.COOKIES
    return HttpResponse(json.dumps(ret_cook))

"""无法获取到kkk999"""
def cook2(request):
    ret_cook = request.COOKIES
    return HttpResponse(json.dumps(ret_cook))


def session(request):

    return HttpResponse('session ok!')