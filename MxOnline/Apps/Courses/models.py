# -*- coding: utf-8 -*-

from datetime import datetime
import os
from django.db import models
from MxOnline import settings

# Create your models here.


def upload_to(instance, filename):
    '''
    让上传的文件路径动态地与model的名字有关
    :param instance: 使用这处upload_to函数的model。
    :param filename: 上传的文件名。
    :return:
    '''
    className = str(type(instance))[:-2].split('.')[-1] # 类名
    nowTime = datetime.now().strftime('%Y-%m-%d')  # 时间
    return os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, className, str(instance), nowTime, filename)


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="课程名称")
    desc = models.CharField(max_length=200, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")  # 目前暂时为TextField,以后支持富文本后再进行修改。
    degree = models.CharField(choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2, verbose_name="课程难度")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(小时)")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    # image = models.ImageField(upload_to='courses/images/%Y/%m', max_length=200, verbose_name="封面图")
    image = models.ImageField(upload_to=upload_to, max_length=200, verbose_name="封面图")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

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
    download = models.FileField(upload_to=upload_to, max_length=200, verbose_name="资源文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
