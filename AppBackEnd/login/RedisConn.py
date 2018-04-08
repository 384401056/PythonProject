#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

class RedisConn:

    def __init__(self, host='127.0.0.1', port=6379, db=0):
        redis_pool = redis.ConnectionPool(host=host, port=port, db=db)
        self.redis = redis.Redis(connection_pool=redis_pool)

    def getConn(self):
        return self.redis