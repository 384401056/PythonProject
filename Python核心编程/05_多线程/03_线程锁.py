from atexit import register
from threading import Thread, currentThread, Lock
from time import sleep, ctime


lock = Lock()
ls = []

def loop(nsec):
    myname = currentThread().name
    ''' 由于对多个线程对同一个变量 ls 进行了操作，所以要有锁机制'''
    # lock.acquire() # 使用with lock(): 可代替
    with lock:
        ls.append(myname)
        print('[%s] Started %s' % (ctime(), myname))
    # lock.release()

    sleep(nsec)

    # lock.acquire()
    with lock:
        ls.remove(myname)
        print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
        print('(remaining: %s)' % (ls or 'NONE'))
    # lock.release()


def main():
    for i in range(0,11):
        Thread(target=loop,args=(4,)).start()

@register
def _atexit():
    print('all done at', ctime())

if __name__ == '__main__':
    main()

