#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    @property
    def width(self):
        """长方形的宽度"""
        return self.x2 - self.x1

    @width.setter
    def width(self,value):
        """设置长方形的宽度。"""
        self.x2 = self.x1 + value

    @property
    def height(self):
        """长方形的高度"""
        return self.y2 - self.y1

    @height.setter
    def height(self, value):
        """设置长方形的高度。"""
        self.y2 = self.y1 + value

    def __repr__(self):
        return "{}({},{},{},{})".format(self.__class__.__name__, self.x1, self.y1, self.x2, self.y2)



def main():
    rect = Rectangle(10, 10, 25, 40)

    #获取高宽
    print(rect.width)
    print(rect.height)
    print(rect)

    # 设置高度
    rect.width = 20
    rect.height = 50

    print(rect.width)
    print(rect.height)
    print(rect)

    # 打印帮助
    print(help(Rectangle))

if __name__ == '__main__':
   main()
