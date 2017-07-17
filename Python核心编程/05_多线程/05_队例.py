''' 便用Queue来完成生产者和消费者的问题  '''

from random import randint
from threading import Thread
from time import ctime, sleep
from queue import Queue


def writeQ(q):
    print('生产一个对象到Q中了...', ctime())
    q.put('xxx',True)
    print('size now',q.qsize())

def readQ(q):
    val = q.get(1)
    print('从Q中取到了一个对象...', ctime())
    print('size now',q.qsize())

def writer(q, loops):
    for i in range(loops):
        writeQ(q)
        sleep(1)

def reader(q, loops):
    for i in range(loops):
        readQ(q)
        sleep(2)

funcs = [writer, reader]
nfunc = range(len(funcs))

def main():
    nloops = randint(2,20)
    q = Queue(32)
    th = []

    for i in nfunc:
        t = Thread(target=funcs[i], args=(q,nloops), name=funcs[i].__name__)
        th.append(t)

    for i in nfunc:
        th[i].start()

    for i in nfunc:
        th[i].join()
    print('全部完成!!!')



if __name__ == '__main__':
    main()
