#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis


def main():
    redis_pool = redis.ConnectionPool(host='192.168.20.131', port=6379)
    r = redis.Redis(connection_pool=redis_pool)

    # r.set('name', 'gaoyanbin', ex=10) # 设置值，10秒缓存

    # r.delete('name') # 删除

    print(r.get('name'))



if __name__ == '__main__':
    main()
