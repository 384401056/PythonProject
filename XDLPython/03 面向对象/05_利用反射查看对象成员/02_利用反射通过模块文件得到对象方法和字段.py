#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    ''' 利用反射通过模块文件得到对象方法和字段 '''

    # 通过反射找到模块
    mod = __import__('Person')
    # 通过模块找到类
    mod_clss = getattr(mod, 'Person')
    # 生成类的对象
    obj = mod_clss('Jims Lily', 20)

    # 通过对象找到类中方法和字段
    func = getattr(obj, 'show')
    attr1 = getattr(obj, 'name')
    attr2 = getattr(obj, 'age')

    # 显示字段
    print(attr1)
    print(attr2)

    # 调用方法
    func()

if __name__ == '__main__':
    main()