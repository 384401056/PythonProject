# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models

from Apps.User.models import UserProfile
from Apps.Courses.models import Course


# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=50, verbose_name="课程名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile,blank=True, null=True,on_delete=models.CASCADE, verbose_name="用户名")
    course = models.ForeignKey(Course,blank=True, null=True, on_delete=models.CASCADE, verbose_name="课程")
    comments = models.CharField(max_length=200, verbose_name="评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="评论时间")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nick_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,blank=True, null=True, on_delete=models.CASCADE, verbose_name="用户")
    fav_id = models.IntegerField(default=0 , verbose_name="数据ID")
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"机构"),(3,"讲师")), default=1, verbose_name="收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nick_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="接收消息的用户") # 如果为0，代表是发给所有人的消息.
    message = models.CharField(max_length=500, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读") # 默认为未读.
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s (%s)' % (self.user.nick_name, self.has_read)


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, null=True,on_delete=models.CASCADE, verbose_name="用户名")
    course = models.ForeignKey(Course, blank=True, null=True,on_delete=models.CASCADE, verbose_name="课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nick_name




















