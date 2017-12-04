from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from . import  models

# Create your views here.

def index(request):

    # =========================增===============================
    # 创建model对象的几种方法.
    # ut1 = models.UserType()
    # ut1.caption = '管理员'
    # ut1.save()
    #
    # ut2 = models.UserType.objects.create(caption='普通用户')
    # ut2.save()
    #
    # user_dict = {'caption':'超级管理员'}
    # ut3 = models.UserType.objects.create(**user_dict)
    # ut3.save()

    # user_info_dict1 = {
    #     'username':'Eric',
    #     'email':'384401056@qq.com',
    #     'pwd':'abc123',
    #     'user_type':models.UserType.objects.get(nid=1)
    # }
    #
    # user1 = models.UserInfo.objects.create(**user_info_dict1)
    # user1.save()
    #
    # user_info_dict2 = {
    #     'username': 'Alex',
    #     'email': '379100129@qq.com',
    #     'pwd': 'def456',
    #     'user_type_id':2  # 外键的字段会自动加上_id
    # }
    #
    # user2 = models.UserInfo.objects.create(**user_info_dict2)
    # user2.save()



    # =========================单表查询===============================

    # ret = models.UserInfo.objects.all() # 返回一个querySet类型的对象
    # print(type(ret), ret.query) # 输出查询的sql语句
    # for item in ret:
    #     print(item.id, item.username, item.email, item.pwd)


    # 排序OderBy
    # ret = models.UserInfo.objects.all().order_by('id') # asc
    # ret = models.UserInfo.objects.all().order_by('-id') # desc
    # print(type(ret), ret.query)  # 输出查询的sql语句
    # for item in ret:
    #     print(item.id, item.username, item.email, item.pwd)



    #
    # for item in ret:
    #     print(item.id,item.username,item.email,item.pwd,item.user_type_id)
    #
    # # 只取指定列的值。
    # ret = models.UserType.objects.all().values('caption')
    # for item in ret:
    #     print(type(item), item) # 此时的item是字典
    #
    # ret = models.UserType.objects.all().values_list('nid','caption')
    # for item in ret:
    #     print(type(item), item) # 此时的item是元组


    #=========================条件查询================================
    # ret = models.UserInfo.objects.filter(username='alex') # 此时querySet是列表类型
    # print(ret[0].username)

    # ret = models.UserInfo.objects.filter(username='alex').first()  # 此时querySet是对象
    # print(type(ret), ret.username)

    # =========================连表查询===============================

    # ret = models.UserInfo.objects.all()
    # for item in ret:
    #     # 此处返回的item.user_type其实是UserType对象。(因为写了__str__()方法所以才有了打印)
    #     # 也就是说，外键字段就直向了一个UserType对象，就可以取出对象中的所有值。
    #     print(item.id, item.username, item.email, item.user_type, item.user_type.caption,item.user_type.nid)
    #
    # # 从UserInfo中查询UserType中的字段。使用外键字段名加 __
    # ret = models.UserInfo.objects.all().values('username', 'user_type__caption')
    # for item in ret:
    #     print(item)
    #     # print(item['user_type__caption']) # 单独取某一字段

    # 查询用户类型是'管理员'的所有用户信息：username， user_type__caption
    # ret = models.UserInfo.objects.filter(user_type__caption = '管理员').values('username', 'user_type__caption')
    # ret = models.UserInfo.objects.filter(user_type__caption__in = ['管理员','普通用户'] ).values('username', 'user_type__caption')
    # ret = models.UserInfo.objects.filter(user_type__caption__contains = '普通').values('username', 'user_type__caption')

    # for item in ret: # 此时, querySet是列表。item是元组
    #     print(item)





    return HttpResponse('OK')












    # temp = loader.get_template('booktest/index_bak.html')
    # return HttpResponse(temp.render())
    # 以上两行合为一行代码
    # return render(request, template_name='booktest/index_bak.html')














