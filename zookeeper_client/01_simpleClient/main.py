#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from kazoo.client import KazooClient
from kazoo.recipe.watchers import ChildrenWatch, DataWatch, PatientChildrenWatch

class ValidatorDetector:
    def __init__(self):
        # 获取Client实例。
        self.zk = KazooClient(hosts="192.168.21.145:2181,192.168.21.144:2181,192.168.21.141:2181", timeout=2)

        # 设置节点监听和数值监听。
        self.my_watch1 = ChildrenWatch(client=self.zk, path="/", func=self.validator_watcher_fun) # func= 设置监听函数，这个监听会一直有效。
        self.my_watch2 = DataWatch(client=self.zk, path="/app7", func=self.data_watch_fun)

        # 初始化连接到zookeeper
        self.zk.start()


    def validator_watcher_fun(self, children):
        """
        监听函数
        :param children: 返回的字节点
        :return:
        """
        print("The children now are:", children)
        # self.zk.get_children("/", )

    def data_watch_fun(self, data, stat, event):
        """监听函数"""
        print("The Node data is Change", data, stat, event)


    def create_node(self):
        """创建节点"""
        self.zk.create('/app-python', b'python_create_node', makepath=True)

    def is_exist(self, path):
        """判断节点是否存在"""
        print("Yes") if (self.zk.exists(path) is not None) else print("No")

        # if self.zk.exists(path) is not None:
        #     print("Yes")
        # else:
        #     print("No")

    def getData(self, path):
        """获取节点上的数据"""
        try:
            ret = self.zk.get(path) # 返回一个元组，第一个元素是value,第二个是Stat
            print("%s : " % path ,ret)
        except:
            print("%s : 无数据 " % path)


    def setData(self, path, value):
        """更新数据"""
        try:
            # 传入的value必须转为byte[]
            self.zk.set(path, bytes(value, encoding='utf8'))
            ret = self.zk.get(path)
            print("更新数据成功。", str(ret[0], encoding='utf8'))
        except Exception as ex:
            print("更新数据失败。",str(ex))


    def delete(self, path):
        """删除节点"""
        try:
            if self.zk.delete(path):
                print("删除 %s 成功" % path)
        except Exception as ex:
            print("删除 %s 失败!" % path, str(ex))


if __name__ == '__main__':
    vd = ValidatorDetector()
    print("connected..")
    # vd.create_node()
    # vd.is_exist('/app7')
    # vd.getData('/app7')
    # vd.delete('/app8')
    # vd.setData('/app7', 'this is app7 data ....')
    time.sleep(100000)
