#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch, DataWatch, PatientChildrenWatch

NODE_GROUP = "/Server"

class DistributedServer:
    """分布式服务器注册类"""

    def __init__(self):
        # 获取Client实例。
        self.zk = KazooClient(hosts="192.168.21.145:2181,192.168.21.144:2181,192.168.21.141:2181", timeout=2)
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
    ds.registerServer("111.111.111.12:8000")

    # 模拟服务器一直在运行，如果断开则节点被删除
    time.sleep(1000000)



if __name__ == '__main__':
    main()


