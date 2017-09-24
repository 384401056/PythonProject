#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    '''进制转换'''

    # 十进制转其它
    b = 15
    print(bin(b))
    print(hex(b))
    print(oct(b))

    # 二进制转十进制
    print(int('1111', base=2))
    print(int('f', base=16))
    print(int('17', base=8))


if __name__ == '__main__':
    main()