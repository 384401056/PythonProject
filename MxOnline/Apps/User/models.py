# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    '''
    用户表
    自定义userprofile表来替换django中自动生成的 user 表
    继承自AbstractUser类，也就是django自动生成的user表中生成的字段。
    '''
    nick_name = models.CharField(max_length=50, default="anonymous", verbose_name="昵称")
    birday = models.DateField(blank=True, null=True, verbose_name="生日")  # 可为空
    gender = models.CharField(choices=(("male", "男"), ("famel", "女")), default="male", max_length=6, verbose_name="性别")
    address = models.CharField(max_length=100, default="", verbose_name="地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号码")  # 可为空
    image = models.ImageField(upload_to="User/images/%Y/%m", default="image/default.png", max_length=200, verbose_name="用户头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username  # 这里的username是继承自AbstractUser的。


class EmailVerifyRecord(models.Model):
    '''
    邮箱验证码
    '''
    code = models.CharField(max_length=20, verbose_name="验证码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=(("register", "注册"),("forget","找回密码")), max_length=10, verbose_name="发送类型")# 用于区分注册和找回密码
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间") # 这里的now不要加(),否则就会以model编译的时间做为默认时，不加()才会以实例化的时间来生成。

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s (%s)' % (self.code, self.email)


class Banner(models.Model):
    '''
    轮播图
    '''
    title = models.CharField(max_length=100,verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m/%d/", verbose_name="轮播图片", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址") # 轮播图的url地址.
    index = models.IntegerField(default=100, verbose_name="顺序") # 轮播图的顺序字段.
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title









