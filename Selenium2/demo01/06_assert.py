#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        print('Test start')
        self.input = input('Enter a number:')
        self.number = int(self.input)

    def test_case_equal(self):
        '''断言相等'''
        self.assertEqual(self.number, 10, 'Your input is not 10')

    def test_case_ture(self):
        '''断言表达式为true'''
        self.assertTrue((self.number > 0),'Your input is not true')

    def test_case_in(self):
        '''断言是否包含'''
        ls = [1,2,3,4,5,6,7,8,9,0]
        self.assertIn(self.number, ls, 'You input is not in list')

    def tearDown(cls):
        print('Test end')


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(MyTest('test_case_in'))

    runner = unittest.TextTestRunner()
    runner.run(suit)