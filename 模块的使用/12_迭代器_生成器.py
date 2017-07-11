links = {'鱼C工作室':'http://www.fishc.com','鱼C论坛':'http://bbs.fishc.com','鱼C博客':'http://blog.fishc.com'}

# for key in links.keys():
#     print(key + ' -> ' + links[key])

it = iter(links) # 创建一个迭代器
# print(next(it));
# print(next(it));
# print(next(it));
# print(next(it)); # 如果没有元素了会报警StopIteration异常

# while True:
#     try:
#         each = next(it)
#     except: # 当报异常时退出程序
#         break
#     print(each)

# 创建自己的Fibonacci数列，包含yield语句的函数会被特地编译成生成器
# 不像一般的函数会生成值后退出，生成器函数在生成值后会自动挂起并暂停他们的执行和状态，
# 他的本地变量将保存状态信息，这些信息在函数恢复时将再度有效
def fibs(maxNum = 10):
    a, b = 0, 1
    while a < maxNum:
        yield a  # 虽然这里返回值a，但后面的代码再下次迭代时又会接着执行。
        a, b = b, a + b

f = fibs(100)
for each in f: # 生成迭代器
    print(each, end=',')


