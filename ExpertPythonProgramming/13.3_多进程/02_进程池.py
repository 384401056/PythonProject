#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time
from multiprocessing import Process, Pool

POOL_SIZE = 6 # 当用6个进程执行是，只要1秒后就能得到所有结果

PLACE = ('Reykjavik', 'Vien', 'Zadar', 'Venice', 'Wroclaw', 'Bolognia')


def work(place):
    time.sleep(1)
    return place+str(random.randint(1, 1000))


def present_result(geocode):
    print(geocode)


def main():
    with Pool(POOL_SIZE) as pool:
        results = pool.map(work,PLACE) # 根据传入的参数，决定执行多少次方法
        # results = pool.apply(work,('Reykjavik',)) # 执行1次方法，传入一个参数。


    print(results)
    # for result in results:
    #     present_result(result)

if __name__ == '__main__':
    main()
