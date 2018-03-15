#!/usr/bin/env python
# -*- coding utf-8 -*-

import pika

EXCHANGE_NAME = 'logs_direct_test'
SERVERITY = 'info'


def main():
    credentials = pika.PlainCredentials('admin', 'admin')  # 创建证书
    # 创建与RabbitMQ的连接池
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.20.130', port=5672, credentials=credentials))

    # 创建频道
    channel = connection.channel()

    # 创建交换机，并设置为广播模式
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct')

    # 创建随机独占队列
    result = channel.queue_declare(exclusive=True)  # exclusive 独占
    queue_name = result.method.queue  # 获取独占队列名

    # 定阅
    channel.queue_bind(
        exchange=EXCHANGE_NAME,
        queue=queue_name,
        routing_key=SERVERITY,
    )

    # 消费者的加调函数
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        ch.basic_ack(delivery_tag=method.delivery_tag)  # 有应答要加上这句

    # 消费者的设置
    channel.basic_consume(callback,
                          queue=queue_name,
                          # no_ack=True,  # 此时无应答
                          no_ack=False,  # 此时有应答
                          )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
