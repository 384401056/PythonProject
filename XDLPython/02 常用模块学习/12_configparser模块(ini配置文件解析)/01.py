#!/usr/bin/env python
# -*- coding utf-8 -*-

import configparser


def main():
    # 创建配置解析对象
    conf = configparser.ConfigParser()
    # 读取配置文件
    conf.read('ini', encoding='utf-8')

    # 获取ini的节点信息
    ret = conf.sections()
    print(ret)

    # 获取节点下的选项
    ret = conf.options('kaixin')
    print(ret)

    # 获取选项的值
    ret = conf.get('kaixin', 'age')
    print(ret)

    ret = conf.getint('kaixin', 'age')  # 在获取值的同时进行类型转换.
    print(ret, type(ret))

    ret = conf.getfloat('kaixin', 'number')
    print(ret, type(ret))

    # 添加节点
    # conf.add_section('kkk')
    # conf.write(open('ini', 'w'))

    # 添加/修改选项（如果选项存在，则是修改）
    # conf.set('kkk', 'name', 'limit')
    # conf.set('kkk', 'age', '130')
    # conf.set('kkk', 'number', '12.323')
    # conf.write(open('ini', 'w'))


    # 删除节点
    # conf.remove_section('kkk')

    # 删除选项
    # conf.remove_option('kkk', 'number')
    conf.write(open('ini', 'w'))





if __name__ == '__main__':
    main()
