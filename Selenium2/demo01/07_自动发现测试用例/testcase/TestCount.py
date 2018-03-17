#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calculator import Count
import unittest

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        print('TestCount start')

    def tearDown(self):
        print("TestCount end!")

class TestCount(BaseTestClass):

    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(20,20)
        self.assertEqual(j.add(),40)

if __name__ == '__main__':
    unittest.main()