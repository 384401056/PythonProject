from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100,  unique=True, verbose_name='发布会标题')
    limit = models.IntegerField(verbose_name='参加人数')
    status = models.BooleanField(verbose_name='状态')
    address = models.CharField(max_length=200, verbose_name='地址')
    start_time = models.DateTimeField(verbose_name='发布会时间')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    def __str__(self):
        return self.name


class Guest(models.Model):
    event = models.ForeignKey(Event) # 关联Even表
    realname = models.CharField(max_length=64, verbose_name='姓名')
    phone = models.CharField(max_length=16, verbose_name='手机号')
    email = models.EmailField(verbose_name='邮箱')
    sign = models.BooleanField(verbose_name='签到状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        unique_together = ("event", "phone") # 设置联合主键

    def __str__(self):
        return self.realname



