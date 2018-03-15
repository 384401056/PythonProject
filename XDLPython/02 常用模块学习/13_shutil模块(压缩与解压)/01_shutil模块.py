#!/usr/bin/env python
# -*- coding utf-8 -*-
import shutil


def f1():
    '''拷贝文件内容, 从源文件拷贝内容到目标文件中，如果目标文件打开方式为 w ,则覆盖，如果为 a ,则为追加'''
    shutil.copyfileobj(open('src.txt', 'r'), open('tar.txt','w'))


def f2():
    '''直接对整个文件进行拷贝'''
    shutil.copyfile('src.txt', 'kkk.txt')



def f3():
    '''创建压缩包，并返回文件路径'''

    # 将当前指定路径下的所有文件，压缩成路径为 my_python_project 格式为zip 的压缩包
    shutil.make_archive('my_python_project', 'zip', 'E:\\PythonProject\\XDLPython\\01 基础')



def main():
    f3()


if __name__ == '__main__':
    main()