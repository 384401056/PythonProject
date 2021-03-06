import dbm

items = [
    ['1', 'Lawnmower', 'Tool', '1', '$150', 'Excellent', '2012-01-05'],
    ['2', 'Lawnmower', 'Tool', '2', '$350', 'Fair', '2012-04-01'],
    ['3', 'Bike', 'Vehicle', '3', '$650', 'Good', '2013-03-22'],
    ['4', 'Drill', 'Tool', '4', '$750', 'Good', '2013-10-28'],
    ['5', 'Scarifier', 'Tool', '5', '$1320', 'Average', '2013-09-14'],
    ['6', 'Sprinkler', 'Tool', '1', '$7150', 'Good', '2014-01-06'],
]

members = [
    ['1', 'Fred', 'fred@lendylib.org'],
    ['2', 'Mike', 'Mike@lendylib.org'],
    ['3', 'Joe', 'Joe@lendylib.org'],
    ['4', 'Rob', 'Rob@lendylib.org'],
    ['5', 'Anne', 'Anne@lendylib.org'],
]

loans = [
    ['1', '1', '3', '4/1/2012', '4/26/2012'],
    ['2', '2', '5', '9/5/2012', '1/5/2013'],
    ['3', '3', '4', '7/3/2013', '7/22/2013'],
    ['4', '4', '1', '11/19/2013', '11/29/2013'],
    ['5', '5', '2', '12/5/2013', 'None'],
]


def createDB(data, dbName):
    try:
        # 创建DBM文件
        db = dbm.open(dbName,'c')
        for datum in data:
            # 用于将序列中的元素以指定的字符连接生成一个新的字符串
            db[datum[0]] = ','.join(datum)
    finally:
        db.close()
        print(dbName,'created')


def readDB(dbName):
    try:
        # 读取DBM文件
        db = dbm.open(dbName,'r')
        print('Reading', dbName)
        return [db[datum] for datum in db]
    finally:
        db.close()


def main():

    print('Creating data files...')
    createDB(items,'itemdb')
    createDB(members, 'memberdb')
    createDB(loans, 'loandb')

    print('Reading data files...')
    print(readDB('itemdb'))
    print(readDB('memberdb'))
    print(readDB('loandb'))


if __name__ == '__main__':
    main()


















