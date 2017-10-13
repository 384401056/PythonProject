#!/usr/bin/env python
# -*- coding utf-8 -*-
import sys
from libs import account

def main():

    ''' 导入自定义模块有两种方法：1.将文件拷贝到调用文件相同目录下。2.sys.path.append("要导入的文件路径") '''

    account.login()
    account.register()
    account.logout()


if __name__ == '__main__':
    main()