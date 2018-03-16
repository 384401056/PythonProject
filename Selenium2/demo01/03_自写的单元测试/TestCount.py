#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calculator import Count

class TestCount:

    def test_add(self):
        try:
            j = Count(5, 20)
            assert (j.add() == 25), 'result error!'
        except AssertionError as e:
            print(e)
        else:
            print('Test pass');

if __name__ == '__main__':
    MyTest = TestCount()
    MyTest.test_add()