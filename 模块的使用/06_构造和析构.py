# 构造方法
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPeri(self):
        return (self.x+self.y)*2

rect = Rectangle(10,20)
print(rect.getPeri())



# new方法，一般情况下，此方法是不用重写的。
class CapStr(str):

    # 重写父类的__new__方法.将构造中带入的字符，返回成大写字符。
    def __new__(cls, s):
        s = s.upper()
        return str.__new__(cls,s)

s = CapStr("i love python")
print(s)




# del析构方法.将对象要被销毁时，才会被调用。（此处的销毁是指垃圾回收机制生效时）
class DelClass:
    def __init__(self):
        print('__init__方法，被调用了')

    def __del__(self):
        print('__del__方法，被调用了')

d1 = DelClass()
d2 = d1
d3 = d2
del d2 # 这两句 del 只是删除了引用。
del d3
del d1 # 此句删除了最后一个引用，垃圾回收就会生效。