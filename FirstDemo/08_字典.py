#创建字典的几种方法

dict1 = dict(zip("xyz","123"))

dict1 = dict(name="gaoyanbin",sex="男",age=20)

dict1 = {'first':1,'second':2}

dict1 = dict([('a',1),('b',2),('c',3),('d',4)])

print(dict1)

t1 = dict1.items()

t1 = dict1.keys();

t1 = dict1.values();


print(t1)