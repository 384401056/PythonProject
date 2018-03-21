
from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from booktest import models
from django.db.models import F,Q,Count
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

    # ---------------------------反向查询,通被外键的表查询关联表的数据：1.在values中表名__字段名  2.python代码中表名_set,得到外键表的列表 ----------------------------------------------

    # ret = models.UserType.objects.filter(caption='管理员').values('caption', 'userinfo__username', 'userinfo__email') # 加了vlues数据就变成了元组了，不再是对象了。
    # ret = models.UserType.objects.filter(caption='管理员').first() # 返回的是单个对象
    # print(type(ret), ret)

    # 当为all时，会例出所有UserType
    # ret = models.UserType.objects.all().values('caption', 'userinfo__username', 'userinfo__email')


    # 返回的是一个列表(元组列表,因为加了values)
    # ret_list = ret.userinfo_set.all().values('user_type__caption', 'user_type__nid', 'username', 'email', 'pwd')
    # for item in ret_list:
    #     print(item)

    # 返回的UserInfo表的列表(对象列表)
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

    # -------------------------------正向操作-------------------------------
    # group_obj = models.Group.objects.get(gid=1)
    # host01 = models.Host.objects.filter(hid__gt=3) # 查找出hid大于3的host对象列表

    # 将hid大于3的host对象,分配给group gid=1 的部门
    # group_obj.h2g.add(*host01)

    # 直接通过已知的hid来添加
    # group01 = models.Group.objects.get(gid=8)
    # group01.h2g.add(*[1, 2, 3, 4])

    # 这里的set只是增加没有的，保留已有的。group01 gid 相同的关系，会被删除。
    # 增加了group01与所有hid>=1的host之间的关系。, 原来的gid相同的，会被删除.
    # 相当于重建group01的与其它host的关系
    # group01.h2g.set(models.Host.objects.filter(hid=1))

    #-------------------------------反向操作-------------------------------
    # 将host对象hid为5的设备分配给，gid为3,4的group对象

    # host02 = models.Host.objects.get(hid=1)
    # print(host02)

    # 将host02分配给gid大于等于2的Group.此时的 表名_set 指的是关联关系表
    # host02.group_set.add(*models.Group.objects.filter(gid__gte=4))

    # 直接通过已知的gid来添加
    # host02.group_set.add(1)
    # host02.group_set.add(*[2,3,4])



    # 删除关联表中，gid大于等于1的数据。
    # host02.group_set.remove(*models.Group.objects.filter(gid__gte=1))
    # host02.group_set.remove(*models.Group.objects.filter(gid__get=1))

    # 自动创建的关联关系表只支持添加、删除，不支持修改。

    # 这里的set只是增加没有的，保留已有的。如果有host02 hid 相同的关系，会被删除。
    # 增加了host02与所有gid>=1的group之间的关系。, 原来的hid相同的，会被删除.
    # 相当于重建host02的与其它group的关系
    # host02.group_set.set(models.Group.objects.filter(gid=3))

    # clear=True 全清除，但是原来的和新加的会一起添加到表中。可以在表中看到,自增id发生了变化。
    # host02.group_set.set(models.Group.objects.filter(gid__gte=1), clear=True)

    # host02 = models.Host.objects.get(hid=4)
    # get_or_create .在group表中添加一个groupname, 并将它与host02建立关系.
    # 如果此groupname与host02已经在关系表中存在，则无变化。
    # r = host02.group_set.get_or_create(groupname ='运维部')
    # print(r)




    #===========================条件查询之 F,Q==========================

    # book01 = models.BookInfo.objects.get(id=1)
    # models.HeroInfo.objects.create(name='edb', age=22, gender=0, content='abcdsfdsaf', book = book01)
    # models.HeroInfo.objects.create(name='aaac', age=20, gender=1, content='abcdsfdsaf', book = book01)
    # models.HeroInfo.objects.create(name='ccc', age=27, gender=0, content='abcdsfdsaf', book = book01)
    # models.HeroInfo.objects.create(name='abbbbc', age=50, gender=1, content='abcdsfdsaf', book = book01)

    # # 在原来age的基础上对age加100，F用来取原来age的值。
    # models.HeroInfo.objects.filter(id=1).update(age=F('age')+100)
    #
    # Q构建搜索条件
    # conn = Q()
    #
    # q1 = Q()
    # q1.connector = 'AND' # q1的搜索关系.
    #
    # q1.children.append(('age',40))
    # q1.children.append(('content','ddddd'))
    #
    # q2 = Q()
    # q2.connector = 'OR'
    # q2.children.append(('name','abc'))
    # q2.children.append(('gender','0'))
    #
    #	
    # conn.add(q1,'AND')
    # conn.add(q2,'AND')
    #
    # ret = models.HeroInfo.objects.filter(conn)
    # for item in ret:
    #     print(item.id, item.name,item.age,item.content,item.gender)


    #==================group by=====================

    # 根据age列来分组，计算数量(id列）,此片的values不再是映射的功能。因为他在annotate前出现
    # ret = models.HeroInfo.objects.all().values('age').annotate(Count('id'))
    # print(ret)


    # ret = {
    #     "name":"gaoyanbin",
    #     "age":100,
    # }

    # return JsonResponse(json.dumps(ret))
    return HttpResponse('Django OK')


    # temp = loader.get_template('booktest/index_bak.html')
    # return HttpResponse(temp.render())
    # 以上两行合为一行代码
    # return render(request, template_name='booktest/index_bak.html')

from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from . import models
from django.db.models import F,Q,Count
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

    # ---------------------------反向查询,通被外键的表查询关联表的数据：1.在values中表名__字段名  2.python代码中表名_set,得到外键表的列表 ----------------------------------------------

    # ret = models.UserType.objects.filter(caption='管理员').values('caption', 'userinfo__username', 'userinfo__email') # 加了vlues数据就变成了元组了，不再是对象了。
    # ret = models.UserType.objects.filter(caption='管理员').first() # 返回的是单个对象
    # print(type(ret), ret)

    # 当为all时，会例出所有UserType
    # ret = models.UserType.objects.all().values('caption', 'userinfo__username', 'userinfo__email')


    # 返回的是一个列表(元组列表,因为加了values)
    # ret_list = ret.userinfo_set.all().values('user_type__caption', 'user_type__nid', 'username', 'email', 'pwd')
    # for item in ret_list:
    #     print(item)

    # 返回的UserInfo表的列表(对象列表)
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

    # -------------------------------正向操作-------------------------------
    # group_obj = models.Group.objects.get(gid=1)
    # host01 = models.Host.objects.filter(hid__gt=3) # 查找出hid大于3的host对象列表

    # 将hid大于3的host对象,分配给group gid=1 的部门
    # group_obj.h2g.add(*host01)

    # 直接通过已知的hid来添加
    # group01 = models.Group.objects.get(gid=8)
    # group01.h2g.add(*[1, 2, 3, 4])

    # 这里的set只是增加没有的，保留已有的。group01 gid 相同的关系，会被删除。
    # 增加了group01与所有hid>=1的host之间的关系。, 原来的gid相同的，会被删除.
    # 相当于重建group01的与其它host的关系
    # group01.h2g.set(models.Host.objects.filter(hid=1))

    #-------------------------------反向操作-------------------------------
    # 将host对象hid为5的设备分配给，gid为3,4的group对象

    # host02 = models.Host.objects.get(hid=1)
    # print(host02)

    # 将host02分配给gid大于等于2的Group.此时的 表名_set 指的是关联关系表
    # host02.group_set.add(*models.Group.objects.filter(gid__gte=4))

    # 直接通过已知的gid来添加
    # host02.group_set.add(1)
    # host02.group_set.add(*[2,3,4])



    # 删除关联表中，gid大于等于1的数据。
    # host02.group_set.remove(*models.Group.objects.filter(gid__gte=1))
    # host02.group_set.remove(*models.Group.objects.filter(gid__get=1))

    # 自动创建的关联关系表只支持添加、删除，不支持修改。

    # 这里的set只是增加没有的，保留已有的。如果有host02 hid 相同的关系，会被删除。
    # 增加了host02与所有gid>=1的group之间的关系。, 原来的hid相同的，会被删除.
    # 相当于重建host02的与其它group的关系
    # host02.group_set.set(models.Group.objects.filter(gid=3))

    # clear=True 全清除，但是原来的和新加的会一起添加到表中。可以在表中看到,自增id发生了变化。
    # host02.group_set.set(models.Group.objects.filter(gid__gte=1), clear=True)

    # host02 = models.Host.objects.get(hid=4)
    # get_or_create .在group表中添加一个groupname, 并将它与host02建立关系.
    # 如果此groupname与host02已经在关系表中存在，则无变化。
    # r = host02.group_set.get_or_create(groupname ='运维部')
    # print(r)




    #===========================条件查询之 F,Q==========================

    # book01 = models.BookInfo.objects.get(id=1)
    # models.HeroInfo.objects.create(name='edb', age=22, gender=0, content='abcdsfdsaf', book = book01)
    # models.HeroInfo.objects.create(name='aaac', age=20, gender=1, content='abcdsfdsaf', book = book01)
    # models.HeroInfo.objects.create(name='ccc', age=27, gender=0, content='abcdsfdsaf', book = book01)
    # models.HeroInfo.objects.create(name='abbbbc', age=50, gender=1, content='abcdsfdsaf', book = book01)

    # # 在原来age的基础上对age加100，F用来取原来age的值。
    # models.HeroInfo.objects.filter(id=1).update(age=F('age')+100)
    #
    # Q构建搜索条件
    # conn = Q()
    #
    # q1 = Q()
    # q1.connector = 'AND' # q1的搜索关系.
    #
    # q1.children.append(('age',40))
    # q1.children.append(('content','ddddd'))
    #
    # q2 = Q()
    # q2.connector = 'OR'
    # q2.children.append(('name','abc'))
    # q2.children.append(('gender','0'))
    #
    #	
    # conn.add(q1,'AND')
    # conn.add(q2,'AND')
    #
    # ret = models.HeroInfo.objects.filter(conn)
    # for item in ret:
    #     print(item.id, item.name,item.age,item.content,item.gender)


    #==================group by=====================

    # 根据age列来分组，计算数量(id列）,此片的values不再是映射的功能。因为他在annotate前出现
    # ret = models.HeroInfo.objects.all().values('age').annotate(Count('id'))
    # print(ret)

    return HttpResponse('Django OK')


    # temp = loader.get_template('booktest/index_bak.html')
    # return HttpResponse(temp.render())
    # 以上两行合为一行代码
    # return render(request, template_name='booktest/index_bak.html')
