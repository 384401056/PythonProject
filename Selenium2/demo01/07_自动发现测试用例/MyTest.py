#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

test_dir = './testcase'

# 根据目录和查找条件，自动发现测试用例.用例的加载顺序是根据ASCII码表的顺序。
discover = unittest.defaultTestLoader.discover(test_dir,'Test*.py', None)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)