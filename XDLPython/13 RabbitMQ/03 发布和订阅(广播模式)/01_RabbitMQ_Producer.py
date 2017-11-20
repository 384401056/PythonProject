#!/usr/bin/env python
# -*- coding utf-8 -*-

import pika
import random

EXCHANGE_NAME = 'cats'


def main():
    credentials = pika.PlainCredentials('admin', 'admin')  # 创建证书
    # 创建与RabbitMQ的连接池
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.20.130', port=5672, credentials=credentials))

    # 创建频道
    channel = connection.channel()

    # 每个交换机在自己独立的进程当中执行，因此增加多个交换机就是增加多个进程
    # 创建交换机,并设置为广播模式.此模式下producer与consumer之间的关系类似与广播电台与收音机，
    # 如果广播后收音机没有接受到，那么消息就会丢失, 所以执久化也就没有意义了。建议先执行consumer.
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')

    # 发布消息
    channel.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key='', # 无队列
        body='Hello RabbitMQ by exchange %s' % EXCHANGE_NAME,
    )

    print('send success msg to rabbitmq')
    connection.close()


if __name__ == '__main__':
    main()
