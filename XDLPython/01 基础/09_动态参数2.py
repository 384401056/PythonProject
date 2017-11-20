#!/usr/bin/env python
# -*- coding utf-8 -*-

# =====================*agrs=========================

# # 从形参的角度看*参数
# def foo(*args):
#     print(args)
# foo(1, 2, 3, 4, 5)  # 其中的2,3,4,5都给了args
#
# # 从实参数的角度看*参数
# def foo(x, y, z):
#     print(x)
#     print(y)
#     print(z)
# foo(*(1, 2, 3))  # 其中的*（1,2,3）拆开来看就是：foo（1,2,3），都按照位置传值分别传给了x,y,z
#
#
# def foo(*args):
#     print(args)
# foo(*(1, 2, 3))



# ===================**kwargs==============================

# # 从形参的角度看**参数
# def foo(**kwargs):
#     print(kwargs)
# foo(y=1, a=2, b=3, c=4)


# 从实参数的角度看**参数
def foo(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# **{"a":2,"b":3,"c":4,"d":5}是将字典里的每个值按照关键字传值的方式传给a,b,c,d
foo(**{"a": 2, "b": 3, "c": 4, "d": 5})


# # 形参与实的参数都使用**的情况
# def foo(**kwargs):
#     print(kwargs)
#
#
# foo(**{"a": 2, "b": 3, "c": 4, "d": 5})
