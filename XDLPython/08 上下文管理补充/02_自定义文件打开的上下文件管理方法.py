#!/usr/bin/env python
# -*- coding utf-8 -*-

import contextlib  # 上下文管理模块


@contextlib.contextmanager
def myopen(fileName, mode):
    f = open(fileName, mode, encoding='utf-8')
    try:
        yield f
    finally:
        f.close()


def main():
    with myopen('111.txt', 'r') as f:
        print(f.readline())


if __name__ == '__main__':
    main()
