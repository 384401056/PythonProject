#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio

async def async_hello(number):
    print(number)


def main():
    # async_obj = async_hell() # 当async方法被调用时，不会执行里面的代码，而是返回一个协和对象

    # 创建一个事件循环来执行aysnc方法。
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.wait(
            [async_hello(number) for number in range(3)], # 生成一个函数列表，打印时可以看到这些函数不是按创建时的顺序执行的。
        )
    )

    loop.close()

if __name__ == '__main__':
    main()