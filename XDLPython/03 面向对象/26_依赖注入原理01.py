#!/usr/bin/env python
# -*- coding utf-8 -*-

"""
当type生成类之前，执行的__call__方法，在类创建之前，生成类方法__init__需要的参数，
这样类在使用时就不用显示的传入参数了。
"""


# 自定义type类
class MyType(type):
    """type在创建类时，会在__call__方法中执行，类的__new__方法和__init__方法"""

    def __call__(self, *args, **kwds):
        """
        此时的self就是类，类就是type的实例对象。(类也是对象)
        """
        # print('type self:', type(self), self) # 此时的self是type对象，也就是类

        obj = self.__new__(self, *args, **kwds)  # type对象(类)的__new__方法(静态方法),才是正真创建类对象的方法。

        # print('obj :', type(obj), obj) # 此时的obj才是正真的类对象


        name = 'gaoyanbin' # 这就是要注入的参数
        age = 20
        my_args = [name, age]

        obj.__init__(my_args)  # 执行类的__init__方法。传入参数到__init__方法中

        return obj  # 返回类对象


class User(metaclass=MyType):  # 指定此类，用我们自定义的type类来创建

    def __init__(self, my_args):
        self.name = my_args[0]
        self.age = my_args[1]

    def get_user(self):
        print(self.name)
        print(self.age)


def main():
    user = User() # type开始创建对象的过程,此时类没有传入参数。
    user.get_user()

if __name__ == '__main__':
    main()
