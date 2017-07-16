from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime
from atexit import register
from random import randrange

lock = Lock()
MAXNUM = 5

# 信号量
candytray = BoundedSemaphore(MAXNUM)

def refill():
    with lock:
        print('Refilling Candy....')
        try:
            candytray.release()
        except ValueError:
            print('Full ,skipping')
        else:
            print('OK!')
def buy():
    with lock:
        print('Buying candy....')
        if candytray.acquire(False):
            print('OK')
        else:
            print('empty, skipping....')

def producer(loops):
    ''' 生产 '''
    for i in range(loops):
        refill()
        sleep(2)


def consumer(loops):
    ''' 消费 '''
    for i in range(loops):
        buy()
        sleep(2)



def main():
    nloops = randrange(10,20)
    print('start at:', ctime())
    print('The Candy Machine (full with %d bars)!' % MAXNUM)
    Thread(target=consumer, args=(randrange(nloops,nloops+MAXNUM+2),)).start()
    Thread(target=producer, args=(randrange(nloops),)).start()


@register
def _atexit():
    print('all done at: ',ctime())

if __name__ == '__main__':
    main()











