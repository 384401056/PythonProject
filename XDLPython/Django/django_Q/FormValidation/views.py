from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from . import models
from django.db.models import F, Q, Count
import json
from .forms import LoginForm
from datetime import datetime,date

# Create your views here.

"""输出数据转为JSON"""
def index(request):
    if request.method == 'POST':
        result = {'status': True, 'msg': '', 'data': None}
        try:
            post_data = request.POST.get('post_data', None)
            if post_data is not None:
                post_data_dict = json.loads(post_data)
                con = Q()
                for k, v in post_data_dict.items():
                    q1 = Q()
                    q1.connector = 'OR'
                    for item in v:
                        q1.children.append((k, item))
                    con.add(q1, 'AND')

                ret = models.Book.objects.filter(con).values('name', 'page', 'price', 'pubdate', 'book_type__caption')
                print(ret)
                ret_list = list(ret)
                result['status'] = True
                result['data'] = ret_list
        except Exception as e:
            result['msg'] = str(e)

        # 使用自定义解析器,解析Django中的DateTimeField和DecimalField
        from .tests import JsonCustomEncoder
        return HttpResponse(json.dumps(result, cls=JsonCustomEncoder))
    else:
        return HttpResponse('get OK!')

"""表单验证01"""
def login(request):
    if request.method == 'POST':
        result = {'status': True, 'msg': '', 'data': None}

        # request.POST.get('username', None)
        # request.POST.get('pwd', None)

        # 创建自定义Form对象
        f = LoginForm(request.POST)

        if f.is_valid():
            result['status'] = True
        else:
            result['status'] = False
            result['msg'] = f.errors

            # 直接打印输出，为html格式。
            # print(f.errors)
            # print(f.errors['username'][0])
            # print(f.errors['pwd'][0])

        result['data'] = f.cleaned_data

        # 使用自定义解析器,解析Django中的DateTimeField和DecimalField
        # from .tests import JsonCustomEncoder
        # return_json = json.dumps(result, cls=JsonCustomEncoder)
        # return HttpResponse(json.dumps(result, cls=JsonCustomEncoder))
        # return render(request, 'login.html', {'return_json':result})
        return render(request, 'app02/login.html', {'error': f.errors})
    else:
        return render(request, 'app02/login.html')


"""表单验证02"""
def login02(request):
    ret_form = LoginForm()
    if request.method == 'POST':

        # 创建自定义Form对象
        f = LoginForm(request.POST)
        if f.is_valid():
            print(f.cleaned_data) # 打印正常数据
        else:
            print(f.errors) # 打印错误信息

        # 将LoginForm，也传到前端html页面中去。
        return render(request, 'app02/login.html', {'error': f.errors,'form':ret_form})
    else:
        return render(request, 'app02/login.html', {'form':ret_form})


"""初始化sqlite数据"""
def init_db(request):

    if request.method == 'POST':
        # models.BookType.objects.create(caption='武功秘籍')
        # models.BookType.objects.create(caption='编程宝典')
        # models.BookType.objects.create(caption='管理指面')
        # models.BookType.objects.create(caption='文学艺术')
        # models.BookType.objects.create(caption='小人书')

        # models.Book.objects.create(name='九阳神功', page=2000, price=5000.34, pubdate=datetime.now(),book_type=models.BookType.objects.get(id=1))
        # models.Book.objects.create(name='Python编程',page=2000,price=5000.34,pubdate=datetime.now(),book_type=models.BookType.objects.get(id=2))
        # models.Book.objects.create(name='管理的艺术',page=2000,price=5000.34,pubdate=datetime.now(),book_type=models.BookType.objects.get(id=3))
        # models.Book.objects.create(name='我这一辈子',page=2000,price=5000.34,pubdate=datetime.now(),book_type=models.BookType.objects.get(id=4))
        # models.Book.objects.create(name='西游记',page=2000,price=5000.34,pubdate=datetime.now(),book_type=models.BookType.objects.get(id=5))
        # models.Book.objects.create(name='独孤九剑',page=2000,price=5000.34,pubdate=datetime.now(),book_type=models.BookType.objects.get(id=1))
        # models.Book.objects.create(name='JAVA编程思想',page=2000,price=5000.34,pubdate=datetime.now(),book_type=models.BookType.objects.get(id=2))
        # models.Book.objects.create(name='时间管理',page=2000,price=5000.34,pubdate=datetime.now(),book_type=models.BookType.objects.get(id=3))
        # models.Book.objects.create(name='三体',page=2000,price=5000.34,pubdate=datetime.now(),book_type=models.BookType.objects.get(id=4))
        # models.Book.objects.create(name='封神榜',page=2000,price=5000.34,pubdate=datetime.now(),book_type=models.BookType.objects.get(id=5))
        return HttpResponse('post OK')
    else:
        return HttpResponse('get OK')












