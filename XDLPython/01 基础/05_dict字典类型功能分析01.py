#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    user_info = {
        'name':'gaoyanbin',
        'age':30,
        'list':['a', 'b', 'c']
    }

    # print(user_info)

    '''索引'''
    # print(user_info['name'])
    # print(user_info['age'])
    # print(user_info['list'])

    '''遍历'''

    # for item in user_info: # 等同于for user in user_info.keys():
    #     print(item) # 得到key
    #
    # print(user_info.keys()) # 获取所有的key
    # print(user_info.values()) # 获取所有的value
    # print(user_info.items()) # 获取所有的key-value

    # for item in user_info.items():
    #     print(item)

    # for key,value in user_info.items():
    #     print(key,':',value)

    '''其它'''
    # user_info.clear() # 清除所有内容

    # print(user_info.get('age1', '123')) # 如果没有取到值,返回None,或取默认值
    # print(user_info['age']) # 如果没有取到值，报错。

    # print('age' in user_info.keys()) # 是否存在某个key

    del(user_info['age']) # 删除元素（键值对）
    print(user_info)

    n = dict.fromkeys(['k1', 'k2', 'k3', 'k4'])
    print(n)
    n['k1'] = ['gao', 'yan', 'bin']
    print(n)


if __name__ == '__main__':
    main()