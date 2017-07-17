''' 当不使用多线程时，我们每次只能做一件事 '''
# def music():
#     for i in range(2):
#         print ("I was listening to music. %s" %ctime())
#         sleep(1)
#
# def move():
#     for i in range(2):
#         print ("I was at the movies! %s" %ctime())
#         sleep(5)
#
# if __name__ == '__main__':
#     music()
#     move()
#     print ("all over %s" %ctime())

'''当使用多线程时'''
# import threading
# from time import ctime,sleep
#
# def music():
#     for i in range(2):
#         print ("I was listening to munisc. %s" % ctime())
#         sleep(2)
#
# def move():
#     for i in range(2):
#         print ("I was at the movies! %s" % ctime())
#         sleep(2)
#
#
# threads = []
# t1 = threading.Thread(target=music,name='Music_Thread')
# threads.append(t1)
# t2 = threading.Thread(target=move,name='Move_Thread')
# threads.append(t2)
#
# if __name__ == '__main__':
#     for t in threads:
#         t.start()
#         t.join()
#     print("all over %s" % ctime())


import threading
from time import ctime,sleep

def test(val):
    sleep(1)
    print(val,"  %s" % ctime())


thds = []

for i in range(0,11):
    th = threading.Thread(target=test,args=[i])
    thds.append(th)

for t in thds:
    t.setDaemon(True) # 将线程声明为守护线程，必须在start() 方法调用之前设置
    t.start()

# for t in thds:
#     t.join() # 用于等待线程终止

'''可代替上面的循环'''
t.join() # 用于等待线程终止,最后一个线程执行完，才执行主线程

print("welcom to main_thread")




# import time, threading
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


























