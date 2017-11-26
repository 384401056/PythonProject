#!/usr/bin/env python
# -*- coding utf-8 -*-

import pika
import random


def main():
    credentials = pika.PlainCredentials('admin', 'admin')  # 创建证书
    # 创建与RabbitMQ的连接池
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.20.130', port=5672, credentials=credentials))

    # 创建频道
    channel = connection.channel()

    # 创建队列
    channel.queue_declare(queue='MegQueue', durable=True)  # durable消息持久化，在RabbitMQ重启后，消息不会丢失。

    # 设置
    channel.basic_publish(
        exchange='',
        routing_key='MegQueue',
        body='Hello RabbitMQ!' + str(random.randint(0, 11)),
        properties=pika.BasicProperties(
            delivery_mode=2,  # 消息持久化,在RabbitMQ重启后，消息不会丢失。
        )
    )

    print('send success msg to rabbitmq')
    connection.close()


if __name__ == '__main__':
    main()
