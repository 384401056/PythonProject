#!/usr/bin/env python
# -*- coding utf-8 -*-

import memcache


def main():
    mem_conn = memcache.Client(['192.168.20.130:11211'], debug=True)

    # memcache分步式的设置方式。
    # mem_conn = memcache.Client([('192.168.20.130:11211',2),  # 设置某一台服务器的权重.
    #                             '192.168.20.131:11211',
    #                             '192.168.20.132:11211',
    #                             '192.168.20.133:11211',
    #                             '192.168.20.134:11211',
    #                             '192.168.20.135:11211'], debug=True)


    # set 设置一个键值，如果不存在则创建，否则修改。
    # mem_conn.set('foo', 'gaoyanbin', 5) # 其中5为超时时间.

    # set_multi 设置多个值.
    # mem_conn.set_multi({'foo':'aaa', 'foo1':'bbb', 'foo2':'ccc'})

    # get_multi 批量获取
    # print(mem_conn.get_multi(['foo', 'foo1', 'foo2']))


    # add 如果key已经存在，则抛出异常。
    # try:
    #     mem_conn.add('foo', 'love')
    #     print(mem_conn.get('foo'))
    # except Exception as ex:
    #     print(ex)

    # replace 修改一个key值，如果此key不存在，则抛出异常。
    # try:
    #     mem_conn.replace('foo1','gaoyanbin')
    #     print(mem_conn.get('foo1'))
    # except Exception as ex:
    #     print(ex)

    # delete 删除一个键值对
    # mem_conn.delete('foo')
    # print(mem_conn.get('foo'))

    # delete 删除多个键值对.
    # mem_conn.delete_multi(['foo', 'foo1', 'foo2'])
    # print(mem_conn.get('foo'), mem_conn.get('foo1'), mem_conn.get('foo2'))


    # append 修改key的值，在后追加内容。
    mem_conn.append('foo', 'After')

    # prepend 修改key的值，在前追加内容。
    mem_conn.prepend('foo', 'Before')
    print(mem_conn.get('foo'))






if __name__ == '__main__':
    main()

















