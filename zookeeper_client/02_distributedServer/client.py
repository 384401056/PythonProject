#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch, DataWatch, PatientChildrenWatch


NODE_GROUP = "/Server"

class DistributedClient:

    def __init__(self):
        # 获取Client实例。
        self.zk = KazooClient(hosts="192.168.21.145:2181,192.168.21.144:2181,192.168.21.141:2181", timeout=2)

        # 设置节点监听和数值监听。
        self.child_watch = ChildrenWatch(client=self.zk, path=NODE_GROUP,func=self.validator_watcher_fun)  # func= 设置监听函数，这个监听会一直有效。

        # 初始化连接到zookeeper
        self.zk.start()

    def validator_watcher_fun(self, children):
        """
        监听函数。如果 /Server 节点添加、删除了子节点，就会触发此函数。会有一定的延时，
        取决于创建 KazooClient 时设置的 timeout
        :param children:
        :return:
        """
        server_list = []

        # 遍历监听函数返回的节点列表，取出子节点中的 value.
        for data in children:
            value=self.zk.get(path=NODE_GROUP+"/"+data)
            server_list.append(value[0])
        print(server_list)


def main():
    dc = DistributedClient()
    time.sleep(100000)

if __name__ == '__main__':
    main()