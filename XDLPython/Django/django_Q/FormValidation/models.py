from django.db import models

# Create your models here.

class BookType(models.Model):
    caption = models.CharField(max_length=32)


class Book(models.Model):
    name = models.CharField(max_length=32)
    page = models.IntegerField()
    # max_digits最大数目的数字，decimal_places存储的小数位数.
    price = models.DecimalField(max_digits=10,decimal_places=2) # 固定精度的十进制数
    pubdate = models.DateTimeField()
    book_type = models.ForeignKey('BookType')