#!/usr/bin/env python
# -*- coding: utf-8 -*-



class MyClass:
    __secret_value = 1 # 当在一个属性前加了__后，就会被立即重命名，__secret_value就被重命名成了：_MyClass__secret_value

    _secret_value2 = 3 # 类的私有属性。只有一个_



def main():
    instance_of = MyClass()
    # ret = instance_of.__secret_value # 无法直接通过原来的名字访问加了__的属性。
    ret = instance_of._MyClass__secret_value # 只有通过这种方法才能访问.
    print(ret)

if __name__ == '__main__':
    main()