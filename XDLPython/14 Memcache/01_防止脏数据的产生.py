#!/usr/bin/env python
# -*- coding utf-8 -*-

import memcache
''' 运行两次程序，只有一个程序的设置key值会生效，另一个会报错 '''

def main():
    mem_conn = memcache.Client(['192.168.20.130:11211'], debug=True, cache_cas=True)

    # mem_conn.set('foo', 100)

    ret = mem_conn.gets('foo') # 获取foo
    print(ret)
    input('>>>>')
    mem_conn.cas('foo', 200) # 设置foo




if __name__ == '__main__':
    main()

















