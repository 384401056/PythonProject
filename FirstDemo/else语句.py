num = int(input("请输入一个数:"))
count = 10

while count > 0:
    i = num % count
    if i == 0:
        print(i)
        print('找到了.....')
        break
    count -= 2
else:  # 如果整个循环没有break过就会执行else中的语句
    print('结束了....')
