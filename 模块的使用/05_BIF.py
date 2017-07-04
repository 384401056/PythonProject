# issubclass(class, classinfo) 判断一个类是否是另一个类的子类
# class A:
#     pass
#
# class B(A):
#     pass
#
# class C:
#     pass
#
# print(issubclass(B,A)) # True
# print(issubclass(B,object)) # True
# print(issubclass(B,C)) # False


# isinstance(object, classinfo) 判断一个对象是否是一个类的实例.
# class AA:
#     pass
#
# class BB:
#     pass
#
# a = AA()
#
# print(isinstance(a,AA)) # True
# print(isinstance(a,object)) # True
# print(isinstance(a,BB)) # False
# print(isinstance(a,(AA,object,BB))) # 只要是元组中其中一个的实例就返回True

# hasattr(object,name) # 判断一个对象是否有某个属性.
class T:
    def __init__(self, x = 0):
        self.x = x

t = T()

print(hasattr(t,'x')) # True 其中属性名要以str的形式传入。



# getattr(object, name[, default]) 返回一个对象指定的属性值是否存在.
# 其中default是，当不存在此属性时的提示信息。
class Y:
    def __init__(self, x = 0):
        self.x = x

y = Y()
getattr(y,'x') # True
print(getattr(y,'age','你所访问的属性不存在!'))

# setattr(object,name,value) 设置对象中指定属性的值，如果属性不存在则会新建一个属性
# 并对属性赋值。
setattr(y,'age',20)
print(y.age)

# delattr(objcet, name) 删除指定属性,如果不存在会抛出异常AttributeError
# 如果存在则删除
delattr(y,'sex')

