from django.db import models

# Create your models here.

class BookInfo(models.Model):
    title = models.CharField(max_length=50) # 字符类型
    pub_time = models.DateTimeField()  # 日期时间类型

    # 输入对象时的显示文本
    def __str__(self):
        return self.title
        # return self.title.encode('utf-8') # 如果出现编码问题用这句。

class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.BooleanField()  # bool类型
    content = models.CharField(max_length=1000)
    book = models.ForeignKey('BookInfo')  # 外键BookInfo的id

    # 输入对象时的显示文本
    def __str__(self):
        return self.name




class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    pwd = models.CharField(max_length=64)
    user_type = models.ForeignKey('UserType') # 外键UserType的nid,并且数据字段名会变为: usre_type_id

    # def __str__(self):
    #     return self.username


class UserType(models.Model):
    nid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=16)

    # def __str__(self):
    #     return self.caption

"""
  传统的数据库中，多对多模式

# 多对多中的关系表.
class HostToGroup(models.Model):
    nid = models.AutoField(primary_key=True)
    hid = models.ForeignKey('Host')
    gid = models.ForeignKey('Group')

# 主机表
class Host(models.Model):
    hid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    hostip = models.CharField(max_length=32)


# 用户组表
class Group(models.Model):
    hid = models.AutoField(primary_key=True)
    groupname = models.CharField(max_length=32)

"""

# Django 中的多对多
# 主机表
class Host(models.Model):
    hid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    hostip = models.CharField(max_length=32)



# 用户组表
class Group(models.Model):
    gid = models.AutoField(primary_key=True)
    groupname = models.CharField(max_length=32)

    # 此语句就代表：Host表与Group表建立了多对多关系。Django会去自动创建第三张关系表。
    # 此语句可以放在Host表中，也可放在Group表中。
    h2g = models.ManyToManyField('Host')











