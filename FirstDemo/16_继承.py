# class Person:
#     name = 'aaa'
#     age = 20
#     sex = '男'
#
#     def hello(self):
#         print('正在调用父类方法...')
#
# # 如果子类中有父的方法，会自动覆盖掉继承的父类方法.
# class Stuent(Person):
#     def hello(self):
#         print('调用自己的方法...')
#
# s = Stuent()
# s.hello()



# 类的继承
# import random as rd
#
# class Fish:
#     def __init__(self):
#         self.x = rd.randint(0,100)
#         self.y = rd.randint(0,200)
#
#     def move(self):
#         self.x += 1
#         self.y += 2
#         print('我的位置是：x = %d, y = %d' % (self.x,self.y))
#
#
# class GoldFish(Fish):
#     pass
#
# class Salmon(Fish):
#     pass
#
# class Carp(Fish):
#     pass
#
# class Shark(Fish):
#
#     # 此处重写了__init__方法，所以Fish的__init__就被三三覆盖了。
#     def __init__(self):
#         # Fish.__init__(self) # 所以要先调用一下父类的初始化方法,此处的self是Shark的对象。
#         super().__init__()  # 可用此句代替上一句代码,就不用传self
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print('鲨鱼吃东西..')
#             self.hungry = False
#         else:
#             print("吃不下了..")
#
# g = GoldFish()
# g.move()
# g.move()
# s = Shark()
# s.eat()
# s.eat()
# s.move()




class Base1:
    def fool(self):
        print('我是foo1,我为Base1代言. ')

class Base2:
    def foo2(self):
        print('我是foo2,我为Base2代言. ')


class Base(Base1,Base2):
    pass

b = Base()
b.fool()
b.foo2()
















