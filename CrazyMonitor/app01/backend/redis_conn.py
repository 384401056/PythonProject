#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

def redis_conn(settings):
    """
    创建redis连接池
    :param settings:
    :return:
    """
    pool = redis.ConnectionPool(host=settings.REDIS_CONN['HOST'], port=settings.REDIS_CONN['PORT'], db=settings.REDIS_CONN['DB'])
    ret = redis.Redis(connection_pool=pool)
    return ret

def main():
    pass


if __name__ == '__main__':
    main()