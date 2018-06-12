from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    '''
    继承自AbstractUser类，也就是django自动生成的user表中生成的字段。
    '''
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="anonymous")
    birday = models.DateField(verbose_name="生日", blank=True, null=True)  # 可为空
    gender = models.CharField(choices=(("male", "男"), ("famel", "女")), default="male")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)  # 可为空
    image = models.ImageField(upload_to="images/%Y/%m/%d/", match="*.png|*.jpg|*.jpeg", recursive=True,
                              default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username # 这里的username是继承自AbstractUser的。
