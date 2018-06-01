#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from app import Foo

class MyTest(unittest.TestCase):
    def test_is_prime(self):
        foo = Foo('kkk', 100)
        self.assertEqual('kkk',foo.getName())
        self.assertEqual(100,foo.getAge())
        unittest.main()

if __name__ == '__main__':
    main()