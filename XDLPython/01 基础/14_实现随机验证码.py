#!/usr/bin/env python
# -*- coding utf-8 -*-

import random


def main():
    '''随机生成4个大写字母,和2个数字'''
    temp = ''
    for i in range(6):
        '''随机在某一位上生成数字,当随机数为1,3,5时生成一个数字'''
        radnum = random.randrange(0,6)
        if (radnum ==1) or (radnum==3):
            rad1 = random.randrange(1,10)
            temp += str(rad1)
        else:
            rad2 = random.randrange(65, 91)
            c = chr(rad2)
            temp += c
    print(temp)


if __name__ == '__main__':
    main()