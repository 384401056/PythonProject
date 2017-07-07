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

# 创建自己的费波那锲数列
class Fibs:

    def __init__(self):
        self.a = 0;
        self.b = 1;

    def __next__(self):
        self.a, self.b = self.b , self.a+self.b

    def __get__(self, instance, owner):
        return instance.a

f =Fibs()

print(next(f))

