# 重写了__add__和__sub__方法
# class New_int(int):
#     def __add__(self, other):
#         return int.__sub__(self,other)
#
#     def __sub__(self, other):
#         return int.__add__(self,other)
#
# a = New_int(10)
# b = New_int(20)
# print(a-b)

# 反运算方法的重写,非主动发起运算的变量进行运算的方法
class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self,other)

a = Nint(20)
b = Nint(30)
print(a+b) # 此运算没有触发反运算方法__radd__
print(1+b) # 触发反运算方法