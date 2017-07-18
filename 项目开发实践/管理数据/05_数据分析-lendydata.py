import itertools as it


items = [
    ['ID', 'Name', 'Description', 'OWnerID', 'Price', 'Condition', 'Registered'],
    ['1', 'Lawnmower', 'Tool', '1', '$150', 'Excellent', '2012-01-05'],
    ['2', 'Lawnmower', 'Tool', '2', '$350', 'Fair', '2012-04-01'],
    ['3', 'Bike', 'Vehicle', '1', '$650', 'Good', '2013-03-22'],
    ['4', 'Drill', 'Tool', '4', '$750', 'Good', '2013-10-28'],
    ['5', 'Scarifier', 'Tool', '5', '$1320', 'Average', '2013-09-14'],
    ['6', 'Sprinkler', 'Tool', '3', '$7150', 'Good', '2014-01-06'],
]

members = [
    ['ID', 'Name', 'Email'],
    ['1', 'Fred', 'fred@lendylib.org'],
    ['2', 'Mike', 'Mike@lendylib.org'],
    ['3', 'Joe', 'Joe@lendylib.org'],
    ['4', 'Rob', 'Rob@lendylib.org'],
    ['5', 'Anne', 'Anne@lendylib.org'],
]

loans = [
    ['ID', 'ItemID', 'BorrowerID', 'DateBorrowed', 'DateReturned'],
    ['1', '1', '3', '4/1/2012', '4/26/2012'],
    ['2', '2', '5', '9/5/2012', '1/5/2013'],
    ['3', '3', '4', '7/3/2013', '7/22/2013'],
    ['4', '4', '1', '11/19/2013', '11/29/2013'],
    ['5', '5', '2', '12/5/2013', 'None'],
]

# 取出Price中的数字部分
def cost(item):
    return int(item[4][1:])

def owner(item):
    return item[3]


# 统计和
def mySum():
    return sum(cost(item) for item in items[1:])

#　统计平均值
def avg():
    return mySum()/(len(items)-1)


# 统计每个人贡献了多少物品
def numbers():
    # 创建一个空字典
    ownerCount = dict()
    for member in members[1:]:
        count = 0
        for item in items[1:]:
            # 如果items中的OwnerID与members中的ID相同则
            if owner(item) == member[0]:
                count+=1
        # 将名字和数量加入字典中
        ownerCount[member[1]] = count
    return ownerCount


def main():
    print('总价格：%.2f' % mySum())
    print('平均价格：%.2f' % avg())
    print(numbers())


    ''' 工具函数 '''

    # count函数与内置的range()函数原理相似,只是count产生无限的数字序列.
    for n in it.count(15,2):
        if n < 40: print(n, end=' ')
        else: break

    # repeat函数是按照指定的次数重复.
    print(list(it.repeat(6,3)))

    # cycle函数会在给定的序列上轮转.
    res1 = []
    res2 = []
    res3 = []
    resources = it.cycle([res1,res2,res3])
    for n in range(100):
        # 每次循环，让res等于res1、res2、res3
        res = next(resources)
        res.append(n)

    print(res1)
    print(res2)
    print(res3)

    # chain函数把所有输入参数连接成一个列表。
    ls = it.chain([1,2,3],'string',[4,5,6,'king'],(7,8,9))
    for i in ls:
        print(i)


if __name__ == '__main__':
    main()




































