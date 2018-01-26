from django.db import models

# Create your models here.

class BxSlider(models.Model):
    name = models.CharField(max_length=64, unique=True, db_index=True, verbose_name='名称') # db_index 如果为真将为此字段创建索引
    img = models.ImageField(upload_to='./static/images/focus/')
    status_choice = {
        '0':'下线',
        '1':'上线',
    }
    status = models.IntegerField(choices=status_choice, default=1, verbose_name='状态')
    href = models.TextField(max_length=256, verbose_name='链接')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        print(self.name)