#计算一个数的阶乘
# def dg(num):
#     if(num>1):
#         return num * dg(num-1)
#     else:
#         return 1
#
# number = int(input("请输入一个正整数:"))
# print("%d 的阶乘是：%d" % (number, dg(number)))


#斐波那契数列
# def fab(num):
#     if num ==1 or num == 2:
#         return 1
#     else:
#         return fab(num-1)+fab(num-2)
# number = int(input("请输入一个正整数:"))
# print("%d 的斐波那契数是：%d" % (number, fab(number)))


#汉诺塔

def hanoi(n,x,y,z):
    if n==1:
        print(x,"--->",z)
    else:
        hanoi(n-1,x,z,y) #将前n-1个盘子从第一个移动到第二个上
        print(x,'--->',z)#将最底下面的最后一个盘子从第一个移到第三个上
        hanoi(n-1,y,x,z)#将第二个上的n-1个盘子移到第三个上


temp = int(input("输入汉诺塔层数："))

hanoi(temp,'X','Y','Z')












