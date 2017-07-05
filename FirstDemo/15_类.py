# 类定义
class Ball:

    # 构造方法
    def __init__(self,name = 'kkk'):
        self.name = name

    def set_name(self,name):
        self.name = name

    def kick(self):
        print("...." + self.name)

# a = Ball("aaaaa")
# a.kick()

class Person:
    name = 'gaoyanbin' # 公有属性
    __age = 20 # 私有属性

    def getAge(self):
        return self.__age

p = Person()
print(p.name)
print(p.getAge())
# Python的私有属性只是被改了一个名字。_类名__属性名,所以说Python是伪私有
print(p._Person__age)




















