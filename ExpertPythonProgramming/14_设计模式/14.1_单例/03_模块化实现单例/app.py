#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mySingleton import mysignleton

"""
其实，python的模块就是天然的单例模式，因为模块在第一次导入时，会生成.pyc文件，
当第二次导入时，就会直接加载.pyc文件，而不会再次执行模块代码。
因此我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象
"""

def main():
    c1 = mysignleton
    c2 = mysignleton

    print(c1)
    print(c2)

    print(c1 is c2)

if __name__ == '__main__':
    main()