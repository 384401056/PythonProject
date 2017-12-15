from django.core.signals import request_finished
from django.core.signals import request_started
from django.core.signals import got_request_exception

from django.db.models.signals import class_prepared
from django.db.models.signals import pre_init, post_init
from django.db.models.signals import pre_save, post_save
from django.db.models.signals import pre_delete, post_delete
from django.db.models.signals import m2m_changed
from django.db.models.signals import pre_migrate, post_migrate

from django.test.signals import setting_changed
from django.test.signals import template_rendered

from django.db.backends.signals import connection_created


# 信号触发时要执行的函数, 参数sender就是触发者
def pre_save_callback(sender, **kwargs):
    print('pre_save callback, 信号触发执行的方法...')
    print(sender, kwargs)

# 注册信号。pre_save代表django的modal对象保存前，自动触发
pre_save.connect(pre_save_callback)



# 自定义信号。
import django.dispatch

my_signal = django.dispatch.Signal(providing_args=["arg1", "arg2"]) # providing_args 定义触发时要传入的参数


def my_signal_callback(sender, **kwargs):
    print('my_signal_callback, 自定义信号触发执行的方法...')
    print(sender, kwargs)

my_signal.connect(my_signal_callback) # 注册信号.