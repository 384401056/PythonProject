#!/usr/bin/env python
# -*- coding utf-8 -*-

from xml.etree import ElementTree
import requests


def f1():
    '''解析网络XML'''

    # 请求一个返回xml格式的API
    response = requests.get('http://wthrcdn.etouch.cn/WeatherApi?citykey=101010100')
    response.encoding = 'utf-8'
    result = response.text
    print(result)

    # 解析XML格式内容
    root = ElementTree.XML(result)
    print(root.tag)

    # root.iter 获取xml中节点名为zhishu的可迭代列表， iter是无限层级的寻找.
    for node in root.iter('zhishu'):
        # 获取节点的名称
        # print(node.tag)

        # 获取节点中的文字内容,find 是在当前节点的子节点中去寻找
        name = node.find('name').text
        value = node.find('value').text
        detail = node.find('detail').text
        print(name, value, detail)

        # 获取节点中的属性字典
        # node.attrib

    for node in root.iter('weather'):
        date = node.find('date').text
        high = node.find('high').text
        low = node.find('low').text
        print(date, high, low)

def f2():
    '''解析本地XML'''
    with open('test.xml','r+', encoding='utf-8') as f:
        # print(f.read())
        root = ElementTree.XML(f.read())

        for node1 in root:
            print(node1)
            for node2 in node1:
                print('   %s' % node2)
                for node3 in node2:
                    print('       %s' % node3)



def main():
    f2()

if __name__ == '__main__':
    main()
