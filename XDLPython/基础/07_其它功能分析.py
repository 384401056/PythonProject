#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    '''enumerate功能分析'''

    li = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

    for item in li:
        print(item)

    # 为可迭代的对象添加序号,第二个参数借到从第几开始
    for key,value in enumerate(li, 0):
        print(key,value)

    inp = input("输入序号：")
    print(li[int(inp)])



def main2():
    '''range 在3.0中 range 等同于2.7中的 xrange '''
    for i in range(0,10,2):
        print(i)


    for i in range(10,0,-1):
        print(i)

def main3():
    '''str int bety'''
    name = '高谚宾'

    # print(len(name))
    #
    # for item in name:
    #     print(item)
    #     byte_list = bytes(item,'utf-8')
    #     print(byte_list) # 以16进制显示
    #     for b in byte_list:
    #         print(b) # 以10进制显示
    #         print(bin(b)) # 以二进制显示

    b1 = bytes(name,'utf-8')
    b2 = bytes(name,'gbk')

    print(b1)
    for b in b1:
        byte = bin(b).split('0b')[1]# 去除'0b'
        print(byte)
        print(int(b))

    print(str(b1, encoding='utf-8'))

    print(b2)
    for b in b2:
        print(bin(b).split('0b')[1])




if __name__ == '__main__':
    main3()