from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from . import models
import json


# Create your views here.

def index(request):
    # =========================增===============================
    # # 创建model对象的几种方法.
    # ut1 = models.UserType()
    # ut1.caption = '管理员'
    # ut1.save()
    #
    # models.UserType.objects.create(caption='普通用户')
    #
    #
    # user_dict = {'caption':'超级管理员'}
    # ut3 = models.UserType.objects.create(**user_dict)
    # ut3.save()
    #
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


    # ---------------------------------条件查询----------------------------------------
    # ret = models.UserInfo.objects.filter(username='alex') # 此时querySet是列表类型
    # print(ret[0].username)

    # ret = models.UserInfo.objects.filter(username='alex').first()  # 此时querySet是对象
    # print(type(ret), ret.username)

    # =========================连表查询(一对一)，外键字段指向表对象 ===============================

    # ret = models.UserInfo.objects.all()
    # for item in ret:
    #     # 此处返回的item.user_type其实是UserType对象。(因为写了__str__()方法所以才有了打印)
    #     # 也就是说，外键字段就直向了一个UserType对象，就可以取出对象中的所有值。
    #     print(item.id, item.username, item.email, item.user_type, item.user_type.caption,item.user_type.nid)
    #
    # # 从UserInfo中查询UserType中的字段。在models中使用时，外键字段名__属性
    # ret = models.UserInfo.objects.all().values('username', 'user_type__caption')
    # for item in ret:
    #     print(item)
    #     # print(item['user_type__caption']) # 单独取某一字段

    # ---------------------------正向查询（用ForeignKey字段所在的表去查）--------------------
    # 查询用户类型是'管理员'的所有用户信息：username， user_type__caption
    # ret = models.UserInfo.objects.filter(user_type__caption = '管理员').values('username', 'user_type__caption')
    # ret = models.UserInfo.objects.filter(user_type__caption__in = ['管理员','普通用户'] ).values('username', 'user_type__caption')
    # ret = models.UserInfo.objects.filter(user_type__caption__contains = '普通').values('username', 'user_type__caption')

    # for item in ret: # 此时, querySet是列表。item是元组
    #     print(item)

    # ---------------------------反向查询,通被外键的表查询关联表的数据：1.在values中表名__字段名  2.python代码中表名_set,得到外键表的队列 ----------------------------------------------

    # ret = models.UserType.objects.filter(caption='管理员').values('caption', 'userinfo__username', 'userinfo__email') # 加了vlues数据就变成了元组了，不再是对象了。
    # ret = models.UserType.objects.filter(caption='管理员').first() # 返回的是单个对象
    # print(type(ret), ret)

    # 当为all时，会例出所有UserType
    # ret = models.UserType.objects.all().values('caption', 'userinfo__username', 'userinfo__email')


    # 返回的是一个队列(元组队列,因为加了values)
    # ret_list = ret.userinfo_set.all().values('user_type__caption', 'user_type__nid', 'username', 'email', 'pwd')
    # for item in ret_list:
    #     print(item)

    # 返回的UserInfo表的队列(对象队列)
    # ret_list = ret.userinfo_set.all()
    # for item in ret_list:
    #     # 对象通过外键字段，就可以取出另一个表中的数据
    #     # print(item.username, item.email, item.pwd, item.user_type.caption)
    #     print(item)

    # 加入条件查询
    # ret_list = ret.userinfo_set.filter(email='384401056@qq.com')
    # for item in ret_list:
    #     # 对象通过外键字段，就可以取出另一个表中的数据
    #     # print(item.username, item.email, item.pwd, item.user_type.caption)
    #     print(item.username, item.email, item.pwd, item.user_type.caption)



    # for item in ret:
    #     # userinfo_set 取到的是与UserType关联的UserInfo对象.
    #     print(item.userinfo_set.all().values('user_type__caption', 'user_type__nid', 'username', 'email'))




    # =========================连表查询(多对多) ===============================

    # 创建数据
    # models.Host.objects.create(hostname='server1', hostip='10.88.20.2')
    # models.Host.objects.create(hostname='server2', hostip='10.88.20.3')
    # models.Host.objects.create(hostname='server3', hostip='10.88.20.4')
    # models.Host.objects.create(hostname='server4', hostip='10.88.20.5')
    # models.Host.objects.create(hostname='server5', hostip='10.88.20.6')
    #
    # models.Group.objects.create(groupname='生产部')
    # models.Group.objects.create(groupname='研发部')
    # models.Group.objects.create(groupname='行政部')
    # models.Group.objects.create(groupname='市场部')


    # group_obj = models.Group.objects.get(gid=1)
    # host01 = models.Host.objects.filter(hid__gt=3) # 查找出hid大于3的host对象队列

    # 将hid大于3的host对象,分配给group gid=1 的部门
    # group_obj.h2g.add(*host01)


    # 将host对象hid为5的设备分配给，gid为3,4的group对象

    host02 = models.Host.objects.get(hid=5)

    # 将host02分配给gid大于等于2的Group.此时的 表名_set 指的是关联关系表
    # host02.group_set.add(*models.Group.objects.filter(gid__gte=2))

    # 删除关联表中，gid大于等于1的数据。
    # host02.group_set.remove(*models.Group.objects.filter(gid__gte=1))
    # host02.group_set.remove(*models.Group.objects.filter(gid__get=1))

    # 自动创建的关联关系表只支持添加、删除，不支持修改。
    # 这里的set只是增加没有的，保留已有的。增加了host02与所有gid>=1的group之间的关系。
    host02.group_set.set(models.Group.objects.filter(gid__gte=1))





    return HttpResponse('OK')







    # temp = loader.get_template('booktest/index_bak.html')
    # return HttpResponse(temp.render())
    # 以上两行合为一行代码
    # return render(request, template_name='booktest/index_bak.html')
