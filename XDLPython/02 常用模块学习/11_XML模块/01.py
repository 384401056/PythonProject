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
    with open('test.xml', 'r+', encoding='utf-8') as f:
        # print(f.read())
        root = ElementTree.XML(f.read())
        for node1 in root:
            print(node1)
            for node2 in node1:
                print('   %s' % node2)
                for node3 in node2:
                    print('       %s' % node3)


def f3():
    '''直接对文件进行解析, 并对XML文件进行修改.'''
    tree = ElementTree.parse('test.xml')
    root = tree.getroot()
    # print(root.tag)
    for node in root.iter('province'):

        # 获取节点属性
        print(node.attrib['id'], node.attrib['name'])

        # 修改节点属性
        node.attrib['name'] = '你的名字被修改'

        # 删除节点属性
        del node.attrib['id']

        # 新增节点属性
        node.set('ID', '000')
        node.set('Age', '999')

        # 获取节点属性的值
        print(node.get('ID'))
        print(node.get('name'))
        print(node.get('Age'))

    # 将所有对文件的修改写入文件
        tree.write('test1.xml', encoding='utf-8')



def f4():
    ''' 创建XML文档 '''

    # 创建根节点
    root = ElementTree.Element('userlist')

    # 创建子节点
    user1 = ElementTree.SubElement(root, 'user', {'enable':'true'})

    # 创建孙节点
    name = ElementTree.SubElement(user1, 'name')
    name.text = 'Jim'
    age = ElementTree.SubElement(user1, 'age')
    age.text = '30'
    sex = ElementTree.SubElement(user1, 'sex')
    sex.text = '男'

    # 用另一种方法，创建子节点
    user2 = root.makeelement('user', {'enable': 'false'})
    # 创建孙节点
    name = ElementTree.SubElement(user2, 'name')
    name.text = 'Lily'
    age = ElementTree.SubElement(user2, 'age')
    age.text = '30'
    sex = ElementTree.SubElement(user2, 'sex')
    sex.text = '女'
    root.append(user2) # 将节点添加到root节点中。


    # 创建ElementTree,用于写入xml文件
    tree = ElementTree.ElementTree(root)
    # short_empty_elements=False 代表空元素不进行自闭合。
    tree.write('new_xml.xml', short_empty_elements=False, encoding='utf-8', xml_declaration=True)

    # file_xml = ElementTree.parse('new_xml.xml')
    # root = file_xml.getroot()
    # print(root.tag)


def main():
    f4()


if __name__ == '__main__':
    main()
