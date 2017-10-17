#!/usr/bin/env python
# -*- coding utf-8 -*-

import tarfile


def f1():
    '''压缩'''

    # 创建一个压缩包，laxi.zip
    tf = tarfile.open('laxi.tar', 'w')
    # 将文件写入压缩包中,将可修改其名字
    tf.add('kkk.txt', arcname='abc.txt')
    tf.add('tar.txt')
    tf.add('src.txt')
    # 关闭文件
    tf.close()

    # # with的形式
    # with zipfile.ZipFile('laxi.zip', 'w') as zf2:
    #   zf2.write('kkk.txt')
    #   zf2.write('tar.txt')


def f2():
    '''解压'''
    tf = tarfile.open('laxi.tar', 'r')
    file_list = tf.list()# 返回压缩包中的文件例表
    print(file_list)

    # # 先获取所有成员
    # mem = tf.getmembers()
    # # 解压所有文件,到指定文件路径，如果目录不存在，会自动创建.
    # tf.extractall('C:\\Users\\Administrator.USER-20160621QE\\Desktop\\laxi', mem)


    mem = tf.getmember('src.txt')
    # 解压src.txt文件到指定文件路径，如果目录不存在，会自动创建.
    tf.extract(mem, 'C:\\Users\\Administrator.USER-20160621QE\\Desktop\\bbb')



def main():
    f2()


if __name__ == '__main__':
    main()