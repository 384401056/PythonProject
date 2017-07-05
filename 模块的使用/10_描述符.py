# class MyDecriptor:
#     def __get__(self, instance, owner):
#         print("__get__ instanc=%s, owner=%s" % (instance,owner))
#
#     def __set__(self, instance, value):
#         print("__set__ instanc=%s, value=%s" % (instance,value))
#
#     def __delete__(self, instance):
#         print("__delete__ instanc=%s" % instance)
#
# class Test:
#     x = MyDecriptor()
#
# t = Test()
# t.x = 10 # 此时打印 __set__
# y = t.x  # 此时打印 __get__
# del t.x  # 此时打印 __delete__

# 自定义描述符类
# class MyProperty:
#
#     def __init__(self,fget,fset,fdel):
#         self.fget = fget
#         self.fset = fset
#         self.fdel = fdel
#
      # 此处的instance是Test类的对象.
#     def __get__(self, instance, owner):
#         return self.fget(instance)
#
#     def __set__(self, instance, value):
#         return self.fset(instance, value)
#
#     def __delete__(self, instance):
#         return self.fdel(instance)
#
#
# class Test:
#
#     def __init__(self):
#         self._x = None
#
#     def getX(self):
#         return self._x
#
#     def setX(self,value):
#         self._x = value
#
#     def delX(self):
#         del self._x
#
#     x = MyProperty(getX,setX,delX)
#
#
#
# t = Test()
# t.x = 200
# print(t.x)
# del t.x


# 练习 温度类，实现华氏度和摄氏度的转换.
class CelProperty:

    def _init(self,value = 26.0):
        self.cel = float(value)

    def __get__(self, instance, owner):
        return self.cel

    def __set__(self, instance, value):
        self.cel = float(value)


class FahProperty:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32 # 取华氏度的值时，其实是取的摄氏度的换算值。

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8 # 设备华氏度的值时，其实对摄氏度的值进行设置。


class Temp:
    cell = CelProperty()
    fah = FahProperty()

t = Temp()
t.cel = 37.77777777777778 # 对摄氏度赋值
print(t.fah) # 取华氏度的值

t.fah = 100
print(t.cel)


















