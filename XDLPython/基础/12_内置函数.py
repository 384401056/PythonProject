#!/usr/bin/env python
# -*- coding utf-8 -*-

def main():
    # abs 返回绝对值
    i = abs(-123)
    print('abs =', i)

    # all 循环参数，如果每个参数都为真，那么all的返回值为真
    i = all([True, False, True, True])
    print(i)

    # any 只有一个真，就返回真
    i = any([True, False])
    print(i)


    # 0,None,"",[],(),{} ==>0,None,空值都为假



    '''排序'''
    li = [5, 4, 3, 2, 1, 54, 100, 67, 8]
    # li.sort() # 排序,直接改变li的顺序
    li2 = sorted(li)  # sorted不改变原来列表的值，会返回一个就的列表.
    print(li)
    print(li2)
    # 字符串排序
    ls = ['1', '39', '20', '你好','中国', '美国', 'A', 'Ord', 'e', 'x', 'y', 'd', 'z', 'n']
    print(sorted(ls))




    class A:
        def __repr__(self):
            return 'hello'

    a = A()
    print(ascii(a))  # 调用对象的__repr__方法

    ch = chr(65)  # 将一个数字转为字符
    num = ord('A')  # 获取字符的ASCII码
    print(ch)
    print(num)

    # 获得1002/25的商和余数组成的元组,主要用于数据分页
    red = divmod(108, 25)
    print(red)

    # 将字符串的表达式转换并执行。
    a = '1 + 3 + 10 +20'
    b = '12*3+3200'
    print('a =', eval(a))
    print('b =', eval(b))
    # 代变量的eval()
    # print(eval('y + 32', {'y': 20}))

    # 执行python代码,无返回值
    # exec('for i in range(10): print(i)')


    '''过滤器 filter'''
    def fun(p):
        return p>=100

    # 将第二个参数中的元素传入第一个参数（函数）中，计算结果为True会被记录
    # 最后返回一个可迭代对象，包含所有为True的元素
    ret = filter(fun, [100, 200, 300, 400, 22, 33, 44, 66])
    # 上面的函数可以用lambda表达式替代
    # ret = filter(lambda x:x>=100, [100, 200, 300, 400, 22, 33, 44, 66])

    for i in ret:
        print(i)

    # 上面的函数可以用lambda表达式替代
    ret = filter(lambda x:x>=100, [100, 200, 300, 400, 22, 33, 44, 66])

    '''map'''
    def fun2(x):
        return x+100
    # 对可迭代列表，循环执行fun2函数。
    ret = map(fun2,[1,2,3,4,5,6])
    for i in ret:
        print(i)


    '''hash'''
    s = '213213k213@!#@!#$@DSFAREWREwrfewrewrdsfewrq#$#@432rfedsfew'
    i = hash(s)
    print('hash =',i)



if __name__ == '__main__':
    main()
