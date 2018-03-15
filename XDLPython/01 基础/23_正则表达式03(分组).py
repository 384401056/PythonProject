#!/usr/bin/env python
# -*- coding utf-8 -*-
import re


def fun_match():
    '''re.match() 只匹配开头的字符串'''
    expression = 'hello wewely 233AKhello hrt A32SFDhot home aiew, diwoef 32  3@#@# k32l3'
    # 不分组
    ret = re.match('h\w+', expression)
    if ret != None:
        print(ret.group())  # 获取匹配到的结果
        print(ret.groups())  # 获取模型中匹配到的分组结果
        print(ret.groupdict())  # 获取模型中匹配到的分组结果（返回字典）

    # 分组
    ret2 = re.match('h(\w+)', expression)  # 此处加了()分组符号，就会对已经匹配的结果进行分组,这里取出了除h以外的字符
    ret2 = re.match('(h)(\w+)', expression)  # 这里取出了h及其它部分,做为元组的两个元素。
    ret2 = re.match('(?P<n1>h)(?P<n2>\w+)', expression)  # 这里取出了h及其它部分,做为字典的值，其中 ?P<n1> 是指定key值.
    if ret != None:
        print(ret2.group())  # 获取匹配到的结果
        print(ret2.groups())  # 获取模型中匹配到的分组结果
        print(ret2.groupdict())  # 获取模型中匹配到的分组结果（返回字典）


def fun_search():
    '''re.search() 浏览全部字符串，匹配第一个符合规则的字符串'''
    expression = 'hello wewely 233AKhello hrt A32SFDhot home aiew, diwoef 32  3@#@# k32l3'

    ret = re.search('a\w+', expression, flags=re.I)  # 其中flags参数用为控制匹配模式.
    ret = re.search('(a)\w+', expression, flags=re.I)
    ret = re.search('(a)(\w+)', expression, flags=re.I)
    ret = re.search('(?P<n1>a)(?P<n2>\w+)', expression, flags=re.I)

    # 此正则的意义是：匹配，以a开头的任意个数字母(\w+)和空格等字符(.*)，并且最后为一个数字(\d)的字符串.
    ret = re.search('a\w+.*\d$', expression, flags=re.I)
    ret = re.search('a(\w+).*(?P<name>\d)$', expression, flags=re.I)  # 分组，并设置key

    if ret != None:
        print(ret.group())  # 获取匹配到的结果
        print(ret.groups())  # 获取模型中匹配到的分组结果 (返回元组)
        print(ret.groupdict())  # 获取模型中匹配到的分组结果（返回字典）


def fun_findall():
    '''re.findall() 逐个字符进行匹配，将所有匹配到的字符串，放在一个列表中'''

    expression = 'hellow alex alex alex area apple fdsioo qouiios'
    ret = re.findall('\d+\w\d+', expression)
    ret = re.findall('a\w+', expression, flags=re.I)
    ret = re.findall('(a\w+)', expression, flags=re.I)  # 效果同上,对于findall来说，大括号在最外层时分组无意义.
    ret = re.findall('a(\w+)', expression, flags=re.I)  # 此时分组有意义

    # ret = re.search('(a)(\w+)', expression)
    # print(ret.group())
    # print(ret.groups())


    # 分组
    ret = re.findall('(a)(\w+(e))(x)', expression)  # findall分组中添加了?P<name>是没有意义的,因为返回的是list,不是dict


    # ret = re.findall(r'(asd)*', 'asdasd') # 返回['asd', '']

    # 默认只拿最后一个字母,因为pattern中只有一个分组符号(),虽然要匹配4次，但找出来的字符被最后一次覆盖了。只有x
    ret = re.findall(r'(\w){4}', 'alex')
    # 这里有4个分组，所以没有被覆盖.
    ret = re.findall(r'(\w)(\w)(\w)(\w)', 'alex')

    ret = re.findall('(\dasd)+', '1asd2asd3asdkk3')

    if ret != None:
        print(ret)


def fun_finditer():
    '''re.finditer() 与findall功能相同,只是他会生成可迭代对象'''
    expression = 'hellow alex alex alex area apple fdsioo qouiios'

    ret = re.finditer('(a)(\w+(e))(?P<name>x)', expression)  # finditer分组中添加了?P<name>对于groupdict是有意义的

    if ret != None:
        print(ret)

        for i in ret:
            print(i, i.group(), i.groups(), i.groupdict())



def main():
    fun_findall()


if __name__ == '__main__':
    main()
