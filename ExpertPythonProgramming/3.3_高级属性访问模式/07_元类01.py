#!/usr/bin/env python
# -*- coding: utf-8 -*-

def method(self):
    return 1

# 创建了一个类对象，type的参数分别是：类名，基类集合（元组），class的方法名称与函数绑定（字典)
# 虽然可以通过type()函数来代替代元类，但通常的做法是使用继承自type的另一个类。
klass = type('MyClass',(object,),{'func':method})


instance = klass() #通过类对象，创建了一个对象
print(instance)
print(instance.func())
print(type(instance))





