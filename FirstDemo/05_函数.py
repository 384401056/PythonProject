# #定义函数
# def myFuntcion01():
#     print("My First function!")
#
# #执行函数
# myFuntcion01()

#不需要指定返回值类型。
# def myFunction02(num1,num2):
#     return num1+num2
#
# addSum = myFunction02(1,3)
#
# print(addSum)

#函数文档
# def myFunction03(num1,num2):
#     '这是一个把两个数相加的函数'
#     print(num1+num2)
#
# myFunction03(10,30)

#关键字参数
# def myFunction04(name,words):
#     print(name+ "->>" +words)
#
# myFunction04('无名','让编程改变世界')
# myFunction04(words="让编程改变世界",name="无名")


#默认参数
# def myFunction05(name='无名',words='让编程改变世界'):
#     print(name + "->>" + words)
#
# myFunction05()
# myFunction05("苍井空")
# myFunction05(words="让综艺节目改变世界")

#收集参数（可变长参数）
# def myFunction06(*parmas):
#     print("参数个数是：", len(parmas))
#     print("参数列表如下：")
#     for i in parmas:
#         print(i,end=" ")
#
# myFunction06(1,3,4,5,"李小龙",23.233)

#函数返回值
# def myFunction07():
#     return 1,2,"李小龙" #多个返回值会作为一个元组去返回
#
# print(myFunction07())



#在函数中修改全局变量会触发屏蔽机制
# count = 10
#
# # def myFunction08():
# #     count = 5; #此变量是Python创建的一个同名局部变量
# #     print(count)
# #
# # myFunction08()
# # print(count) #全局变量依然是10
#
# def myFunction08():
#     global count  #此语句让函数内修改全局变量成为可能
#     count = 5; #此变量就是全局变量。
#     print(count)
#
# myFunction08()
# print(count)



#内部函数(嵌套函数)
# def fun1():
#     print("Fun1正在被调用...")
#
#     def fun2():
#         print("Fun2正在被调用...")
#
#     fun2()
#
# fun1()


#闭包
# def fun1():
#     x = 5
#     def fun2():
#         nonlocal x
#         x *= x
#         return x
#     return fun2()
#
# print(fun1())

#lambda返回的是一个函数(匿名函数)
func = lambda x:2 * x + 1

func = lambda x,y:x+y

print(func(5,10))










