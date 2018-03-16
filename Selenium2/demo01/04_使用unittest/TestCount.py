#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calculator import Count
import unittest


class TestCount(unittest.TestCase):

    def setUp(self):
        super().setUp()

    '''unittest.main() 用Testloader类会自动寻找以test开头的方法'''
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def tearDown(self):
        super().tearDown()
        print("test end!")


if __name__ == '__main__':
    unittest.main()
