#!/usr/bin/env python
# -*- coding utf-8 -*-


def f1():
    '''百分号方法 %[(name)][flags][width].[precision]typecode '''
    '''
    typecode的种类：
        s，获取传入对象的__str__方法的返回值，并将其格式化到指定位置
        r，获取传入对象的__repr__方法的返回值，并将其格式化到指定位置
        c，整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；字符：将字符添加到指定位置
        o，将整数转换成 八  进制表示，并将其格式化到指定位置
        x，将整数转换成十六进制表示，并将其格式化到指定位置
        d，将整数、浮点数转换成 十 进制表示，并将其格式化到指定位置
        e，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（小写e）
        E，将整数、浮点数转换成科学计数法，并将其格式化到指定位置（大写E）
        f， 将整数、浮点数转换成浮点数表示，并将其格式化到指定位置（默认保留小数点后6位）
        F，同上
        g，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是e；）
        G，自动调整将整数、浮点数转换成 浮点型或科学计数法表示（超过6位数用科学计数法），并将其格式化到指定位置（如果是科学计数则是E；）
        %，当字符串中存在格式化标志时，需要用 %%表示一个百分号
    '''

    s = 'I am %s , age is %d' % ('Lily', 20)  # 普通按顺序的形式
    s = 'I am %(name)s , age is %(age)d' % {'age': 30, 'name': 'Jim'}  # 加了key的形式,可以不按顺序传值。
    s = 'I am %+10s , age is %05d' % ('Lily', 20)  # 添加了占位符的形式,%s右对齐，%d为5位，空位用0占位
    s = 'I am %-10s , age is % 5d' % ('Lily', 20)  # 添加了占位符的形式,%s左对齐，%d为5位，空位用 占位
    s = 'I am %s , age is %010.2f' % ('Lily', 20.8954)  # %f为保留两位小数.
    print(s)


def f2():
    '''format方法 {[[fill]align][sign][#][0][width][,][.precision][type]}'''
    s = 'i am {}'.format(20)
    s = 'i am {:b}'.format(20)  # 二进制
    s = 'i am {:#o}'.format(20)  # 八进制
    s = 'i am {:#x}'.format(20)  # 八进制
    s = 'i am {:%}'.format(0.2)  # 百分比
    s = 'i am {:.2%}'.format(0.2)  # 百分比保留两位
    # print(s)

    s1 = "i am {}, age {}, {}".format("seven", 18, 'alex')  # 按顺序
    s1 = "i am {0}, age {1}, really {0} , mybe {1}".format("seven", 18)  # 指定顺序
    s1 = 'i am {name}, age {age}'.format(name='sever', age=20) # 按名称

    s1 = "i am {}, age {}".format(*["seven", 18, 'alex'])  # 使用列表
    s1 = "i am {name}, age {age}".format(**{'name':'seven', 'age':200})  # 使用字典

    print(s1)


def main():
    f2()


if __name__ == '__main__':
    main()
