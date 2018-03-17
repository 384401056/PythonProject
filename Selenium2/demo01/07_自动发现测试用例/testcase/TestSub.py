#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calculator import Count
import unittest

class BaseTestClass(unittest.TestCase):
    def setUp(self):
        print('TestSub start')

    def tearDown(self):
        print("TestSub end!")

class TestSub(BaseTestClass):
    def test_sub1(self):
        j = Count(12, 3)
        self.assertEqual(j.sub(), 9)

    def test_sub2(self):
        j = Count(30,20)
        self.assertEqual(j.sub(),10)

if __name__ == '__main__':
    unittest.main()