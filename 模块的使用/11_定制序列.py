# 自定义不可变列表
class MyList:

    def __init__(self, *args):
        self.ls = [x for x in args if type(x)==int] # 通过列表推导式，循环取出参数中的值，生成列表.
        self.times = {}.fromkeys(range(len(self.ls)),0) # 用一个字典来存放每个元素被访问的次数，key为数字，起始值为0

    def __getitem__(self, key):
        self.times[key] += 1  # 对字典赋值+1
        return self.ls[key]

    def __len__(self):
        return len(self.ls)


ml = MyList(3,2,3,4,5,6,'a','b','c','d',33,224,665)
print('列表元素个数:',len(ml))
print(ml[0])
print(ml[1])
print(ml[7])
print(ml[8])
print('列表元素被访问次数:',ml.times)