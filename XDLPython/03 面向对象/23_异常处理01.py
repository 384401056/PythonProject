#!/usr/bin/env python
# -*- coding utf-8 -*-


def f1():
    '''捕捉多种类型的异常'''
    mylist = []
    mylist.append('aaaaaa')
    inp = input("输入数字：")

    try:
        n = int(inp)
        l = mylist[n]
        print(l)
    except ValueError:
        print('输入的不是数字')
    except IndexError:
        print('列表索引值错误')
    except Exception as e: # 捕捉所有异常。Exception是所有错误类的基类
        print(e)


def f2():
    '''标准的异常处理代码块.'''
    try:
        pass
    except:  # 如果报错，执行这里的代码块
        pass
    else:
        pass # 如果没有报错，执行这里的代码块
    finally:
        pass # 无论有没有报错，都会执行这里的代码块


def main():
    f1()


if __name__ == '__main__':
    main()
