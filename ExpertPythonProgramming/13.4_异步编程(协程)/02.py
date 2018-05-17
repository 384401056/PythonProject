#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import time
import random

async def waiter(name):
    # time_to_sleep = random.randint(1,3) / 4
    time_to_sleep = 3
    print("{} waited {} seconds".format(name, time_to_sleep))
    # time.sleep(time_to_sleep) # 使用此代码会出现等待,不是异步执行
    await asyncio.sleep(time_to_sleep)  # 使用此代码是异步执行。
    print("{} sleep over..".format(name))


async def main():
    await asyncio.wait(
        [waiter("foo"), waiter("bar")],  # 生成一个函数列表
    )

if __name__ == '__main__':
    # 创建一个事件循环来执行aysnc方法。
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()