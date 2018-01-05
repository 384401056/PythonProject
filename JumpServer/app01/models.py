from django.db import models

# Create your models here.

class Host(models.Model):
    """主机"""
    pass

class HostGroup(models.Model):
    """主机组"""
    pass

class UserProfile(models.Model):
    """堡垒机账号信息"""
    pass


class HosteUser(models.Model):
    """主机登录账号信息"""
    pass