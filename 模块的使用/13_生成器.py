# 当函数中有yield关键时，此函数就是一个生成器
# def myGen():
#     print("生成器被执行")
#     yield 1
#     yield 2
#
# gen = myGen()
# print(next(gen)) # 第一次执行到 yield 1
# print(next(gen)) # 第二次执行到 yield 2


# 生成器完成的费波那切数列
# def fibs():
#     a = 0
#     b = 1
#     while True:
#         a, b = b, b+a
#         yield a # 返回a值
#
# for each in fibs(): # 调用生成器
#     if each > 1000:
#         break
#     print(each, end=' ')

# 生成器推导式,生成一个迭代器
i = (x for x in range(10))

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
for each in i:
    print(each)