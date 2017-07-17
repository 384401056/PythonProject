import pickle

anItem = ['2', 'Lawnmower', 'Tool', '2', '$350', 'Fair', '2012-04-01']

# wb 以二进制文件模式写入数据
with open('item.pickle','wb') as pf:
    pickle.dump(anItem,pf)

with open('item.pickle','rb') as pf:
    itemCopy = pickle.load(pf)

print(itemCopy)