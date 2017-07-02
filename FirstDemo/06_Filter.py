#filter过滤器
#第一个参数是function,第二个参数是一个迭代器类型
ft = filter(None,[1,0,False,True]) #将0和False过滤



def odd(x):
    return x%2
ft = filter(odd,[0,1,2,3,4,5,6,7,8,9,10])

#用lambda来取代上面的代码
ft = filter(lambda x:x%2,range(11))
print(list(ft))




