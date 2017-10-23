#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    '''集合就是不允许重复的列表'''
    li = [111, 111, 111, 444, 555, 666]
    print(li)
    s1 = set(li) # 创建集合
    print("s1=",s1)

    s2 = {11,22,33,44,55,66,77,88,99} # 创建集合
    s2.add(555)  # 添加元素
    print("s2=",s2)

    s1.remove(444) # 移除元素，如果没找到报错。
    s1.discard(444) # 移除元素，没找到也不会报错
    print(s1)

    s1.clear() # 清空集合
    print("s1=",s1)


def main2():

    s1 = {11,22,33,44,55,66,77}
    s2 = {44,55,66,22,33,99,88}

    '''差集判断'''
    ret = s1.difference(s2)  # 返回s1中存在但s2中不存在的。
    print("ret=", ret)

    # s1.difference_update(s2) # 返回s1中存在但s2中不存在的,并更新s1的值
    # print("s1=",s1)
    '''交集判断'''
    ret = s1.intersection(s2)  # 返回交集
    # s1.intersection_update(s2)  # 返回交集，并更新。
    print("ret=", ret)

    '''子集判断'''
    print(s2.issubset(s1)) # 判断s2是否为s1的子集

    '''父集判断'''
    print(s1.issuperset(s2)) # 判断s1是否为s2的父集

    '''对称交集'''
    ret1 = s1.difference(s2)
    ret2 = s2.difference(s1)
    print('ret1=',ret1)
    print('ret2=',ret2)
    # 返回对称集，对称交集就是在两个集合中都独有的。
    ret3 = s1.symmetric_difference(s2)
    print('ret3=',ret3)

if __name__ == '__main__':
    main2()