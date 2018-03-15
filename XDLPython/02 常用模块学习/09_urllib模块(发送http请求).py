#!/usr/bin/env python
# -*- coding utf-8 -*-
from urllib import request
import json

def main():
    result = request.urlopen('http://www.weather.com.cn/data/sk/101110101.html')
    json_str = str(result.read(), encoding='utf-8')
    print(json_str)

    # json.loads() 将字符串转换为字典、列表和元组的方法。json.loads()中的字符串必须使用 "" 双引号。
    ret_dict = json.loads(json_str)
    print(ret_dict) # 注意：python中的字典对象，默认是 '' 单引号
    print(ret_dict['weatherinfo']['city'])


    print(json.dumps(ret_dict)) # json.dumps()将对象转为json字符串.json字符串都是"" 双引号。

if __name__ == '__main__':
    main()