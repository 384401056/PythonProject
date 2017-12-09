from django.db import models

# Create your models here.


class Signal_User(models.Model):
    username = models.CharField(max_length=16)