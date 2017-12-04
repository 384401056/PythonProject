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
    gender = models.BooleanField()  # bool类型
    content = models.CharField(max_length=1000)
    book = models.ForeignKey(BookInfo)  # 外键BookInfo的id

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
