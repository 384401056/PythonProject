# -*- coding: utf-8 -*-


from datetime import datetime
from django.db import models
from utils import upload_file


# Create your models here.



class CityDict(models.Model):
    name = models.CharField(max_length=10, verbose_name="城市名称")
    desc = models.CharField(max_length=200, verbose_name="城市描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="机构名称")
    desc = models.CharField(max_length=200, verbose_name="机构描述")
    category = models.CharField(max_length=20, verbose_name="机构类别", default="pxjg",choices=(("pxjg", "培训机构"), ("gx", "高校"), ("gr", "个人")))
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    # image = models.ImageField(upload_to='courseOrg/images/%Y/%m', max_length=200, verbose_name="封面图")
    image = models.ImageField(upload_to=upload_file.upload_to,blank=True, null=True, max_length=200, verbose_name="封面图")
    address = models.CharField(max_length=200, verbose_name="机构地址")
    city = models.ForeignKey(CityDict,blank=True, null=True, on_delete=models.CASCADE, verbose_name="所在城市")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,blank=True, null=True, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(max_length=20, verbose_name="教师名称")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=50, verbose_name="公司名称")
    work_position = models.CharField(max_length=20, verbose_name="公司职位")
    points = models.CharField(max_length=100, verbose_name="教学特点")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_num = models.IntegerField(default=0, verbose_name="点击量")
    # image = models.ImageField(upload_to='teacher/images/%Y/%m', max_length=200, verbose_name="封面图")
    image = models.ImageField(upload_to=upload_file.upload_to,blank=True, null=True, max_length=200, verbose_name="封面图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name
