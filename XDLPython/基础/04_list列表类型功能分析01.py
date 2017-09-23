#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    # name_list = list()
    name_list = ['gaoyanbin', 'alex', 'jims', 'King']
    # print(name_list)
    # print(name_list[0])
    # print(len(name_list))
    # print(name_list[0:len(name_list)])
    #
    # name_list.append("alex") # 追回
    # print(name_list)
    # print(name_list.count('alex')) # 统计数量
    #
    name_list.extend(['aaa', 'bbb', 'cccc']) # 扩展list
    print(name_list)
    #
    # print(name_list.index('aaa')) # 获取某个元素的索引
    #
    # name_list.insert(0,'First') # 从指定位置插入元素
    # print(name_list)

    # a1 = name_list.pop() # 取出并移除
    # print(a1)
    # print(name_list)

    name_list.remove('bbb') # 移除元素
    print(name_list)

    del(name_list[1]) # 根据下标移除元素
    print(name_list)






if __name__ == '__main__':
    main()

















