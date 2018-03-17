#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calculator import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print('test start')

    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 15)

    def test_add2(self):
        j = Count(20,20)
        self.assertEqual(j.add(),40)

    def tearDown(self):
        print("test end!")


if __name__ == '__main__':
    # 创建测试套件
    suite = unittest.TestSuite()
    # 添加测试用例
    suite.addTest(TestCount('test_add1'))

    # 创建测试执行
    runner = unittest.TextTestRunner()
    # 运行测试套件
    runner.run(suite)