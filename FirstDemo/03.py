#创建列表
member = ['小红','小明','小张','默认']

#数字列表
intlist = list(range(0,100))

#空列表
empty = []

#多类型列表
mixlist = [1,'李小龙',3.14,[1,2,3]]

mixlist.append("黄飞鸿") #追加数据
mixlist.extend(["方世玉","洪熙官"]) #扩展数据
mixlist.insert(1,'严咏春') #插入数据

#删除元素
mixlist.remove('严咏春')
mixlist.remove(mixlist[0])
del member[0]
name = mixlist.pop() #取出最后一个元素

#列表分片
newlist = mixlist[1:4]
newlsit = mixlist[:4] #从列表开始到位置4
newlist = mixlist[3:] #从列表3位置到最后
newlist = mixlist[:]  #获取一个列表的拷贝


#创建元组
mytuple = (1,2,3,4,5,6,7,8,9)
mytuple = (1,) #只有一个元素的元组。
