
# class Tortoise:
#     def __init__(self,x = 1):
#         self.num = x
#
# class Fish:
#     def __init__(self,x = 1):
#         self.num = x
#
# # 类的组合形式
# class Pool:
#     def __init__(self, x, y):
#         self.tortoise = Tortoise(x)
#         self.fish = Fish(y)
#
#     def print_num(self):
#         print("乌龟:",self.tortoise.num)
#         print("金鱼:",self.fish.num)
#
# p = Pool(10,30)
# p.print_num()



# 类对象
# class C:
#     count = 0
#
# a = C();
# b = C();
# c = C();
#
#
# print(a.count)
# print(b.count)
# print(c.count)
# print("------------------------")
#
# C.count = 100
#
# print(a.count)
# print(b.count)
# print(c.count)
# print("------------------------")
#
#
# # 当实例对继承的类属性赋值后，就可生成自己的属性，此值不在随类属性的改变而改变。
# # 只有没有对类属性赋值的实例，其继承的属性才会随类属性的改变而改变
# a.count = 222
# b.count = 999
#
#
# print(a.count)
# print(b.count)
# print(c.count)
# print(C.count)
# print("------------------------")



# 如果属性的名字与方法相同，会把方法覆盖掉.
# 所以在定义类时要注意：属性名用名词，方法名用动词.
class Test:
    def name(self):
        print("我是一个方法")

t = Test()
t.name = 2
print(t.name)

# 此时已经不存在name()方法了。
t.name()


















