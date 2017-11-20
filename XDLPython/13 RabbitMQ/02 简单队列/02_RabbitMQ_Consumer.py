#!/usr/bin/env python
# -*- coding utf-8 -*-

import pika


def main():
    credentials = pika.PlainCredentials('admin', 'admin')  # 创建证书
    # 创建与RabbitMQ的连接池
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.20.130', port=5672, credentials=credentials))

    # 创建频道
    channel = connection.channel()

    # 创建队列
    channel.queue_declare(queue='MegQueue', durable=True) # durable消息持久化，在RabbitMQ重启后，消息不会丢失。

    # 消费者的加调函数
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        ch.basic_ack(delivery_tag=method.delivery_tag)  # 有应答要加上这句

    # 消费者的设置
    channel.basic_consume(callback,
                          queue='MegQueue',
                          # no_ack=True,  # 此时无应答
                          no_ack=False,  # 此时有应答
                          )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
