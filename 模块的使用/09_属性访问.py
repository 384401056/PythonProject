# 创建一个有访问、修改和删除属性方法的类
# 通过property定义一个变量来替代对象属性的访问。
# class Test:
#
#     def __init__(self,num = 0):
#         self.num = num
#
#     def getNum(self):
#         return self.num
#
#     def setNum(self,value):
#         self.num = value
#
#     def delNum(self):
#         del self.num
#
#     n = property(getNum,setNum,delNum);
#
#
# t = Test(10)
# print(t.n) # 相当于调用getNum()
# t.n = 200  # 相当于调用setNum()
# print(t.n)

# 访问对象属性时，内部调用的方法.
# class Test:
#
#     # 当一个属性被访问时.
#     def __getattribute__(self, item):
#         print('__getattribute__')
#
#     # 试图访问一个找不到的属性时.
#     def __getattr__(self, item):
#         print('__getattr__')
#
#     # 当一个属性被设置时
#     def __setattr__(self, key, value):
#         print('__setattr__')
#
#     # 当一个属性被删除时
#     def __delattr__(self, item):
#         print('__delattr__')
#
# t = Test()
# print(t.x)
# t.x = 10
# del t.x


# 练习：写一个矩形类，默认有宽和高两个属性.
# 如果为一个叫square的属性赋值，那么说明这是一个正方形。
class MyRect:

    def __init__(self,width = 1,height = 1):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        # 如果对square进行设置，则对宽和高都赋值同样的值。
        if key == 'square':
            self.width = value
            self.height = value
        else:
            # 调用基类的__setattr__方法。(注意)
            super().__setattr__(key,value)

    def getArea(self):
        print('Area is :',self.width * self.height)


rect = MyRect()
rect.square = 10
rect.getArea()






