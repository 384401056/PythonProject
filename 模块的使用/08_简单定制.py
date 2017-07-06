# 创建一个类，计算在开始运行start方法后和运行stop方法时，用时多少.
import time as time

class Timer:

    def __init__(self):
        self.promp = '未开始计时'


    def start(selfs):
        selfs.start_time = time.perf_counter()
        # selfs.start_time = t.localtime()
        print('计时开始')

    def stop(self):
        self.stop_time = time.perf_counter()
        # self.stop_time = t.localtime()
        self._clac()
        print('计时结束')

    # 计算时间差
    def _clac(self):
        self.promp = "%.2f" % (self.stop_time - self.start_time)

    def __str__(self):
        # 重写__str__方法
        return '共运行了:' + self.promp

    __repr__ = __str__



t = Timer()
t.start()

# 循环用来耗时
for index in range(70000000):
    pass
 
t.stop()
print(t)