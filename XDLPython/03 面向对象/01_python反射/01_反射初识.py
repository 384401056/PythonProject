#!/usr/bin/env python
# -*- coding utf-8 -*-

'''
反射：
    通过字符串的形式导入模块。
    通过字符串的形式去对象中寻找指定成员。
    通过字符串的形式去对象中判断成员是否存在。
    通过字符串的形式去对象中设置成员。
    通过字符串的形式去对象中删除成员。

总结：反射就是通过字符串的形式去对象（模块）中，操作其成员。
'''


def f1():
    ''' 根据用户输入，来导入相应的模块'''
    imp = input("请输入模块：")

    # 通过模块名（字符串）来导入模块.
    com = __import__(imp)
    print(com, type(com))

    f = input("请输入要执行的方法名或属性名：")

    # 判断此方法或者属性，是否存在于模块中。
    if hasattr(com, f):
        # 通过函数名，来查找和执行函数。
        attr = getattr(com, f)
        print(type(attr))

        # 执行方法
        try:
            ret = attr()
            # 打印结果
            if ret is not None:
                print(ret)
        except Exception as ex:  # 如果是属性则打印属性
            print(attr)


def f2():
    ''' 删除属性,此处的删除只是针对内存中的模块，不会修改原模块中的属性'''
    imp = input("请输入模块：")
    com = __import__(imp)
    f = input("请输入要删除的方法名或属性名：")
    if hasattr(com, f):
        # 通过属性名删除属性。
        delattr(com, f)
        print('删除属性成功。')
    else:
        print('属性不存在。')


def f3():
    ''' 设置属性,此处的设置只是针对内存中的模块，不会修改原模块'''
    imp = input("请输入模块：")
    com = __import__(imp)
    f = input("请输入要设置的属性名：")
    if not hasattr(com, f):
        # 通过名称设置属性， 并指定值。
        setattr(com, f, 18)
        print('属性设置成功。')
    else:
        print('属性已经存在。')

    # 执行方法/属性
    try:
        ret = getattr(com, f)
        # 打印结果
        if ret is not None:
            print(ret)
    except Exception as ex:  # 如果是属性则打印属性
        print(attr)


def f4():
    ''' 设置方法,此处的设置只是针对内存中的模块，不会修改原模块'''
    imp = input("请输入模块：")
    com = __import__(imp)
    f = input("请输入要设置的方法名：")
    if not hasattr(com, f):
        # 通过名称设置方法，my_func为自定义的函数.
        setattr(com, f, my_func)
        print('设置方法成功。')
    else:
        print('方法已经存在。')

    # 执行方法
    try:
        func = getattr(com, f)
        ret = func(com)
        # 打印结果
        if ret is not None:
            print(ret)
    except Exception as ex:  # 如果是属性则打印属性
        print(func)


def my_func(com):
    '''自定义的函数，用于加到模块中'''
    return ("这是一个新增到 %s 模块中的方法" % com.__name__)  # 输出模块的名称


def f5():
    # 通过模块名（字符串）来导入模块。如果模块不在当前目录下，则：
    com = __import__('lib.test.commons2', fromlist=True)
    print(com, type(com))
    attr = getattr(com, 'f1')
    ret = attr()
    print(ret)


def main():
    f4()


if __name__ == '__main__':
    main()
