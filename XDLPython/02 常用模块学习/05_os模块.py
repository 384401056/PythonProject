#!/usr/bin/env python
# -*- coding utf-8 -*-
import os

'''os主要是跟操作系统有关的模块'''


def main():
    os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录路径
    os.stat('path/filename')  # 获取文件/目录信息
    os.stat('path/filename').st_size  # 获取文件大小
    os.sep  # 操作系统特定的路径分隔符，win下为"\\", Linux下为"/
    os.linesep  # 当前平台使用的行终止符，win下为"\t\n", Linux下为"\n"
    os.system("bash command")  # 运行shell命令，直接显示

    os.name  # 字符串指示当前使用平台。win->'nt';Linux->'posix'

    os.path.split('path')  # 将path分割成目录和文件名二元组返回
    os.path.dirname('path')  # 返回path的目录。其实就是os.path.split(path)的第一个元素
    os.path.basename('path')  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

    os.path.exists('path')  # 如果path存在，返回True；如果path不存在，返回False

    os.path.isfile('path')  # 如果path是一个存在的文件，返回True。否则返回False
    os.path.isdir('path')  # 如果path是一个存在的目录，则返回True。否则返回False

    os.path.getatime('path')  # 返回path所指向的文件或者目录的最后存取时间
    os.path.getmtime('path')  # 返回path所指向的文件或者目录的最后修改时间


if __name__ == '__main__':
    main()
