#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

def redis_conn(settings):
    """创建redis连接池"""
    pool = redis.ConnectionPool(host=settings.REDIS_CONN['HOST'], port=settings.REDIS_CONN['PORT'])
    ret = redis.Redis(connection_pool=pool)
    return ret

def main():
    pass


if __name__ == '__main__':
    main()