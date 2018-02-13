#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    '''数学运算符'''
    val1 = 9 + 2
    val2 = 9 - 2
    val3 = 9 * 2
    val4 = 9 / 2
    val5 = 9 % 2
    val6 = 9 // 2  # 地板除
    print(val6)




def main2():
    '''比较运算符'''
    if 2 == (4-2):
        print("==")
    else:
        print("!=")

    if 3 >= (4-2):
        print("<=")
    else:
        print("Not")

    if 2 <= (4-2):
        print(">=")
    else:
        print("Not")


def main3():
    '''赋值运算符'''
    a = 123
    b = 245
    c = 23
    d = 230
    a += 10;
    b -= 10;
    c /= 10;
    d *= 10;
    d %= 10;
    print(a)

def main4():
    '''逻辑运算符'''
    # and or not
    pass


def main5():
    '''成员运算符'''
    s = 'Alex SB'
    ret = 'Al' in s
    print(ret)

    li = ['alex', 'lily', 'jim']
    ret = 'Hello' not in li
    print(ret)



if __name__ == '__main__':
    main5()