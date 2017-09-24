#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    # abs 返回绝对值
    i = abs(-123)
    print('abs =', i)

    # all 循环参数，如果每个参数都为真，那么all的返回值为真
    i = all([True, False, True, True])
    print(i)

    # any 只有一个真，就返回真
    i = any([True, False])
    print(i)

    '''排序'''
    li = [5, 4, 3, 2, 1, 54, 100, 67, 8]
    # li.sort() # 排序,直接改变li的顺序
    li2 = sorted(li)  # sorted不改变原来列表的值，会返回一个就的列表.
    print(li)
    print(li2)
    # 字符串排序
    ls = ['1', '39', '20', '你好','中国', '美国', 'A', 'Ord', 'e', 'x', 'y', 'd', 'z', 'n']
    print(sorted(ls))





if __name__ == '__main__':
    main()
