from django.contrib import admin
from booktest.models import *


# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    # 设置列表视图
    list_display = ['id', 'title', 'pub_time']


class HeroInfoAdmin(admin.ModelAdmin):
    # 设置列表视图
    list_display = ['id', 'name', 'gender', 'content', 'book']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
