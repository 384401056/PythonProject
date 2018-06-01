#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
为了使类只能出现一个实例，我们可以使用__new__来控制实例的创建过程
'''
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        '''
        重载父类的__new__方法
        '''
        if cls._instance is None:
            # 如果为空，则调用父类静态方法创建对象
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class ConcreateClass(Singleton):
    pass

def main():

    # 创建的两个对象，实则是同一个。
    # c1 = Singleton()
    # c2 = Singleton()
    #
    # print(c1)
    # print(c2)
    #
    # if c1 == c2:
    #     print("True")
    # else:
    #     print("False")

    """
    这种简单的单列模式，是有漏洞的，当实现了单例的类，成为另人的父类时，这时就会出问题。也就非安全子类化
    """
    cc = ConcreateClass() # 先生成子类
    c1 = Singleton() # 再生成父类， 这时会发现生成了两个对象。

    # c1 = Singleton()  # 先生成父类.
    # cc = ConcreateClass()  # 再生成子类，这时会发现只生成了1个对象。

    print(cc)
    print(c1)

    print(cc is c1)


if __name__ == '__main__':
    main()