from django.db import models
from django.contrib.auth.models import (
    User, BaseUserManager,AbstractBaseUser, PermissionsMixin
)

# Create your models here.

class Host(models.Model):
    """主机"""
    hostname = models.CharField(max_length=64, verbose_name='主机名')
    ip_addr = models.GenericIPAddressField(unique=True, verbose_name='IP地址')
    port = models.PositiveIntegerField(default=22, verbose_name='登陆端口')
    idc = models.ForeignKey('IDC', verbose_name='所在机房')
    enabled = models.BooleanField(default=True, verbose_name='是否启用')

    def __str__(self):
        return '%s:%s' % (self.hostname, self.ip_addr)


class HostGroup(models.Model):
    """主机组"""
    name = models.CharField(max_length=64, unique=True, verbose_name='主机组名')
    bind_hosts = models.ManyToManyField('BindHost')

    def __str__(self):
        return self.name


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """堡垒机用户信息"""
    email = models.EmailField(
        max_length=255,
        unique=True,
        null=True,
        verbose_name='邮件地址'
    )

    password = models.CharField(max_length=128)
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_active

    def __str__(self):
        return self.email



class HostUser(models.Model):
    """主机账号信息如 root用户,密码...、mysql用户"""
    auth_type = models.SmallIntegerField(choices=auth_type_choices, default=0, verbose_name='认证方式')
    auth_type_choices = (
        (0,'ssh-password'),
        (1,'ssh-key'),
    )
    
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128, blank=True, null=True) # 当选择认证方式为ssh-key时就不用密码。

    # 字段联合唯一约束
    class Meta:
        unique_together = ('auth_type', 'username', 'password')

    def __str__(self):
        return self.username

class BindHost(models.Model):
    """主机和主机账号的绑定关系表"""
    host = models.ForeignKey('Host')
    host_user = models.ForeignKey('HostUser')

    # 字段联合唯一约束
    class Meta:
        unique_together = ('host', 'host_user',)

    def __str__(self):
        return '%s:%s' % (self.host, self.host_user)


class IDC(models.Model):
    """机房信息"""
    name = models.CharField(max_length=64, unique=True)  # 机房名

    def __str__(self):
        return self.name