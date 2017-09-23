#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    # abs 返回绝对值
    i = abs(-123)
    print('abs =',i)

    # all 循环参数，如果每个参数都为真，那么all的返回值为真
    i = all([True,False,True,True])
    print(i)

    # any 只有一个真，就返回真
    i = any([True,False])
    print(i)




if __name__ == '__main__':
    main()