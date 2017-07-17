import threading
from time import ctime, sleep

'''第一种方法：创建Thread的实例，传给它一个函数'''
# # 线程中要执行的方法
# def loop(nloop,nsec):
#     print('线程: %s' % str(nloop),'开始于 [%s]' % ctime())
#     sleep(nsec)
#     print('线程：%s' % str(nloop),'结束于 [%s]' % ctime())
#
# ths = []
#
# def main():
#     for i in range(0,11):
#         th = threading.Thread(target=loop,name='loopThread',args=(i,2))
#         ths.append(th)
#
#     for th in ths:
#         th.start()
#
#     for th in ths:
#         th.join()
#
#     print('所有线程执行完毕，于[%s]' % ctime())
#
# if __name__ == '__main__':
#     main()

'''第二种方法：创建 Thread 的实例，传给它一个可调用的类实例'''

# class MyThread():
#     def __init__(self,func,args,name=''):
#         self.name = name
#         self.args = args
#         self.func = func
#
#     # 一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()
#     # 当调用一个对象的实例时，就会执行__cal__()函数
#     # 在Python中，对象和函数的区别并不显著
#     def __call__(self, *args, **kwargs):
#         self.func(*self.args)
#
# def loop(nloop,nsec):
#     print('线程: %s' % str(nloop),'开始于 [%s]' % ctime())
#     sleep(nsec)
#     print('线程：%s' % str(nloop),'结束于 [%s]' % ctime())
#
# ths = []
#
# def main():
#     for i in range(0,11):
#         # 对target的赋值是一个类的实例（对象），类的实例也是可调用的。
#         th = threading.Thread(target=MyThread(loop,(i,2),'loop_thread'))
#         ths.append(th)
#
#     for th in ths:
#         th.start()
#
#     for th in ths:
#         th.join()
#
#     print('所有线程执行完毕，于[%s]' % ctime())
#
# if __name__ == '__main__':
#     main()



'''第三种方法，派生 Thread 的子类，并创建子类的实例'''

class MyThread(threading.Thread):

    def __init__(self,func,args,name=''):
        ''' 调用父类的__init__()方法 '''
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func

    def run(self):
        ''' 当线程执行时，调用的方法 '''
        self.func(*self.args)# self.args是一个元组


def loop(nloop,nsec):
    print('线程: %s' % str(nloop),'开始于 [%s]' % ctime())
    sleep(nsec)
    print('线程：%s' % str(nloop),'结束于 [%s]' % ctime())

ths = []

def main():
    for i in range(0,11):
        # 使用自定义的类来创建线程实例.
        th = MyThread(loop,(i,2),'loop_thread')
        ths.append(th)

    for th in ths:
        th.start()

    for th in ths:
        th.join()

    print('所有线程执行完毕，于[%s]' % ctime())

if __name__ == '__main__':
    main()
















