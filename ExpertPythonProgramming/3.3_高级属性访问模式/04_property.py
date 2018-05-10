#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
property简化了描述符的编写，但在使用继承时必须小心。property属性是根据当前类的方法实时创建的，
无法通过覆写父类方法来改变property, 只能在子类中覆写整个property(但使用父类的方法),但这样在可维护性上又有问题。
如里真的要使用这种方法，最好在子类中覆写整个property包括其中的方法。
其实property的最佳语法是使用property装饰器。
"""



class Rectangle(object):
    """
    定义一个正方形的类。
    """

    def __init__(self, x1, y1, x2, y2):
        '''
        初始化传入2个点的坐标。
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        '''
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def _width_get(self, ):
        '''
        计算出宽度
        :return:
        '''
        return self.x2 - self.x1

    def _width_set(self, value):
        '''
        设置长方形的宽度。
        :param value:
        '''
        self.x2 = self.x1+value

    def _height_get(self):
        return self.y2 - self.y1

    def _height_set(self, value):
        self.y2 = self.y1 + value

    width = property(
        _width_get, _width_set, doc="长方形的宽度"
    )

    height = property(
        _height_get, _height_set, doc="长方形的高度"
    )

    def __repr__(self):
        return "{}({},{},{},{})".format(self.__class__.__name__, self.x1, self.y1, self.x2, self.y2)



def main():
    rect = Rectangle(10, 10, 25, 40)

    #获取高宽
    print(rect.width)
    print(rect.height)
    print(rect)

    #设置高度
    rect.width = 20
    rect.height = 50

    print(rect.width)
    print(rect.height)
    print(rect)

    #打印帮助
    print(help(Rectangle))

if __name__ == '__main__':
    main()





