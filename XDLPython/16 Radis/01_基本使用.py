#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis


def main():
    redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=redis_pool)

    # r.set('name', 'gaoyanbin', ex=10) # 设置值，10秒缓存
    # r.set('name', 'gaoyanbin', px=1000) # 设置值，1000毫秒缓存

    # r.set('name', 'gaoyanbin12321', nx=True) # 添加，如果key存在，则不操作。

    # r.set('age', '10')
    # r.set('age', '12', xx=True) # 修改，如果key存在，则操作。否则不操作

    # r.delete('name') # 删除
    # print(r.get('name'))
    # print(r.get('age'))

    # 批量设置
    # r.mset({'name':'jims','age':30, 'add':'世纪生活园左岸公寓...'})

    # print(r.get('name'))
    # print(r.get('age'))
    # print(str(r.get('add'), encoding='utf-8'))

    # 批量获取
    # print(r.mget('name', 'age', 'add'))

    # 获取设置前的值，并设置新值
    # old_value = r.getset('name', 'constantin')
    # print(old_value)
    # print(r.get('name'))

    # 在value后追加内容
    # r.append('name', 'gaoyanbin')
    # print(r.get('name'))

if __name__ == '__main__':
    main()
