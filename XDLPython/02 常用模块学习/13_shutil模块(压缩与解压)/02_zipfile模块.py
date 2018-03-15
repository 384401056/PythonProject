#!/usr/bin/env python
# -*- coding utf-8 -*-

import zipfile


def f1():
    '''压缩'''

    # 创建一个压缩包，laxi.zip
    zf = zipfile.ZipFile('laxi.zip', 'w')
    # 将文件写入压缩包中
    zf.write('kkk.txt')
    zf.write('tar.txt')
    zf.write('src.txt')
    # 关闭文件
    zf.close()

    # # with的形式
    # with zipfile.ZipFile('laxi.zip', 'w') as zf2:
    #   zf2.write('kkk.txt')
    #   zf2.write('tar.txt')


def f2():
    '''解压'''
    zf = zipfile.ZipFile('laxi.zip', 'r')
    file_list = zf.namelist() # 返回压缩包中的文件例表
    print(file_list)

    # 解压所有文件,到指定文件路径，如果目录不存在，会自动创建.
    # zf.extractall('C:\\Users\\Administrator.USER-20160621QE\\Desktop\\')

    # 解压kkk.txt文件到指定文件路径，如果目录不存在，会自动创建.
    # zf.extract('kkk.txt', 'C:\\Users\\Administrator.USER-20160621QE\\Desktop\\bbb')



def main():
    f2()


if __name__ == '__main__':
    main()


















