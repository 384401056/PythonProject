#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''模板引擎的本质，就是将html文件内容转换成一个函数，然后为函数提供全局变量，最后执行函数'''

namspace = {'name': 'gaoyanbin', 'data': [11, 22, 33],}

code = '''def hellocute():print('name is %s, age is %d' % (name, data[0]))'''

# 将字符串转为可执行的代码
func = compile(code, '<string>', 'exec')

# 将func函数放入namespace字典中,其中函数名hellocute就是字典的key，代码就是value。
# 此时，对于hellocaute()函数来说，原来字典中的name,data就成了全局变量，可供hellocaute()函数使用了。
exec(func, namspace)

# 执行函数
namspace['hellocute']()
