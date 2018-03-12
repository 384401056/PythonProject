#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
简单工厂模式

内容：不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例。

角色：
    工厂角色（Creator）
    抽象产品角色（Product）
    具体产品角色（Concrete Product）

优点：
    隐藏了对象创建的实现细节
    客户端不需要修改代码

缺点：
    违反了单一职责原则，将创建逻辑几种到一个工厂类里
    当添加新产品时，需要修改工厂类代码，违反了开闭原则
'''

from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    """抽象产品角色"""
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    """具体产品角色"""
    def __init__(self, enable_yuebao=False):
        self.enable_yuebao = enable_yuebao

    def pay(self, money):
        if self.enable_yuebao:
            print("余额宝支付%s元" % money)
        else:
            print("支付宝支付%s元" % money)


class ApplePay(Payment):
    """具体产品角色"""
    def pay(self, money):
        print("苹果支付%s元" % money)


class PaymentFactory:
    """工厂角色"""
    def create_payment(self, method):
        if method == "alipay":
            return Alipay()
        elif method == 'yuebao':
            return Alipay(enable_yuebao=True)
        elif method == "applepay":
            return ApplePay()
        else:
            raise NameError(method)


def main():
    f = PaymentFactory()
    p = f.create_payment("applepay")
    # p = f.create_payment("alipay")
    # p = f.create_payment("yuebao")
    p.pay(100)



if __name__ == '__main__':
    main()