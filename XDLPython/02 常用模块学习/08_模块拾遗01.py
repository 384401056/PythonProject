#!/usr/bin/env python
# -*- coding utf-8 -*-

'''这是文件的注释, 存在全局变量 __doc__ 中'''

print(vars())
print(__doc__)
print(__file__)
print(__package__)  # 文件所在的文件夹路径。当前文件此值为None
print(__cached__)  # 文件的缓存，当前文件此值为None
print(__name__)
print(__builtins__) # 内置函数就在buildtins中

