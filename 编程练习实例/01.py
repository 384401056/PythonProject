''' 简述：这里有四个数字，分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？ '''

for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x != y) & (x != z) & (y != z):
                print(x,y,z)
