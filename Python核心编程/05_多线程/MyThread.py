import threading
from time import ctime, sleep

class MyThread(threading.Thread):
    ''' 自定义的线程类 '''
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func

    def run(self):
        print('线程开始：', self.name, ' at:', ctime())
        self.res = self.func(*self.args)
        print('线程结束：', self.name, ' at:', ctime())

def main():
    pass

if __name__ == '__main__':
    main()

# def nameFunc(num,key,value):
#     print(num, key, value)
#
# def run(func,args):
#     func(*args)
#
# run(nameFunc,(1000,'abc',123))