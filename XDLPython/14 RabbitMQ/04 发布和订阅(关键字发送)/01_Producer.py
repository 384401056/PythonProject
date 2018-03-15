#!/usr/bin/env python
# -*- coding utf-8 -*-

import pika
import random

EXCHANGE_NAME = 'logs_direct_test'
SERVERITY = 'info'  # 关键字


def main():
    credentials = pika.PlainCredentials('admin', 'admin')  # 创建证书
    # 创建与RabbitMQ的连接池
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.20.130', port=5672, credentials=credentials))

    # 创建频道
    channel = connection.channel()

    # 创建交换机,并设置为关键字发送
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct')

    msg = 'Hello RabbitMQ by %s:%s' % (EXCHANGE_NAME, SERVERITY)

    # 发布消息
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=SERVERITY,  # 指定关键字
        body=msg,
    )

    print('开始发送:%s:%s' % (SERVERITY, msg))
    connection.close()


if __name__ == '__main__':
    main()
