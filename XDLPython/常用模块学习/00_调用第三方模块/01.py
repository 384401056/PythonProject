#!/usr/bin/env python
# -*- coding utf-8 -*-

import sys


def main():
    # 打印系统路径, 也是python导入包时的查询路径。
    for path in sys.path:
        print(path)


if __name__ == '__main__':
    main()