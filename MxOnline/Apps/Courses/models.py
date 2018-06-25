# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from utils import upload_file
from Apps.Organization.models import CourseOrg, Teacher
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="课程名称")
    desc = models.CharField(max_length=200, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")  # 目前暂时为TextField,以后支持富文本后再进行修改。
    degree = models.CharField(choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2, verbose_name="课程难度")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(小时)")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    # image = models.ImageField(upload_to='courses/images/%Y/%m', max_length=200, verbose_name="封面图")
    image = models.ImageField(upload_to=upload_file.upload_to, blank=True, null=True,max_length=200, verbose_name="封面图")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    course_org = models.ForeignKey(CourseOrg, blank=True, null=True, on_delete=models.CASCADE, verbose_name="机构") # 课程所属机构
    category = models.CharField(max_length=20, default="其它", verbose_name="课程类别")

    # 此字段用来进行课程搜索时，打的标签。
    tag = models.CharField(max_length=50, default="", verbose_name="课程标签字段")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name


    def get_lesson_nums(self):
        """
        反向外键查询，本课程的章节数。
        :return: 章节数
        """
        return self.lesson_set.all().count()


    def get_learn_user(self):
        """
        反向外键查询，学习本课程的用户。
        :return: 用户QuerySet,前6个
        """
        return self.usercourse_set.all()[:6]


    def __str__(self):
        return self.name


class Lesson(models.Model):
    # on_delete = models.CASCADE 代表级联删除，django2.0与之前的1.8不同之处
    course = models.ForeignKey(Course,blank=True, null=True, on_delete=models.CASCADE, verbose_name="所属课程")  # 外键
    name = models.CharField(max_length=50, verbose_name="章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Video(models.Model):
    lesson = models.ForeignKey(Lesson,blank=True, null=True, on_delete=models.CASCADE, verbose_name="所属章节")  # 外键
    name = models.CharField(max_length=50, verbose_name="视频名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,blank=True, null=True, on_delete=models.CASCADE, verbose_name="所属课程")  # 外键
    name = models.CharField(max_length=50, verbose_name="资源名称")
    # download = models.FileField(upload_to='static/Courses/resource/%Y/%m', max_length=200, verbose_name="资源文件")
    download = models.FileField(upload_to=upload_file.upload_to,blank=True, null=True, max_length=200, verbose_name="资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
