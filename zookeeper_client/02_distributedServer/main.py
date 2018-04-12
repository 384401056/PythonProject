#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch, DataWatch, PatientChildrenWatch

NODE_GROUP = "/Server"

class DistributedServer:
    """分布式服务器注册类"""

    def __init__(self):
        # 获取Client实例。
        self.zk = KazooClient(hosts="192.168.21.136:2181,192.168.21.137:2181,192.168.21.138:2181", timeout=2)
        # 初始化连接到zookeeper
        self.zk.start()


    def registerServer(self, hostname):
        """
        在zookeeper集群中注册服务器
        :param hostname: 主机名
        :return:
        """
        # 创建为暂时有序列号的节点。
        ret = self.zk.create(NODE_GROUP+'/server', value=bytes(hostname,encoding='utf8'), ephemeral=True, sequence=True, makepath=True)
        print("%s is onLine!" % hostname, " path: %s" % ret)



def main():

    # 获取zookeeper连接
    ds = DistributedServer()

    # 利用zk连接注册服务器信息
    ds.registerServer("")



    time.sleep(1000000)


if __name__ == '__main__':
    main()


