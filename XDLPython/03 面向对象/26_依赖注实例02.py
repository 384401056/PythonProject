#!/usr/bin/env python
# -*- coding utf-8 -*-


class Mapper:
    # 类属性
    __mapper_relation = dict()

    # 类方法
    @staticmethod
    def register(cls, value):
        """注册类名，并设置类对应的参数值"""
        Mapper.__mapper_relation[cls] = value

    @staticmethod
    def exist(cls):
        """判断类名是否注册"""
        if cls in Mapper.__mapper_relation:
            return True
        return False

    @staticmethod
    def getValue(cls):
        """获取类名对应的参数"""
        return Mapper.__mapper_relation[cls]


class MyType(type):
    def __call__(self, *args, **kwds):
        obj = self.__new__(self, *args, **kwds)  # type对象(类)的__new__方法(静态方法),才是正真创建类对象的方法。

        args_list = list(args)

        # 根据类名不同，传入不同的参数。
        if Mapper.exist(self):
            args_list.append(Mapper.getValue(self))
        obj.__init__(*args_list, **kwds)  # 执行类的__init__方法。传入参数到__init__方法中

        return obj  # 返回类对象


class Foo(metaclass=MyType):  # 指定此类，用我们自定义的type类来创建
    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        print(self.obj)


class Bar(metaclass=MyType):  # 指定此类，用我们自定义的type类来创建
    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        print(self.obj)


def main():
    # 依赖注入
    Mapper.register(Foo, {'name': 'Foo', 'age': 20})
    Mapper.register(Bar, {'name': 'Bar', 'age': 20})

    f = Foo()
    b = Bar()

    f.get_obj()
    b.get_obj()


if __name__ == '__main__':
    main()
