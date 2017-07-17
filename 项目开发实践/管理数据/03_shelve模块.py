import shelve
''' shelve 模块的示例 '''

class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

a = Test(1,2)
b = Test('a', 'b')

shelf = shelve.open('test.shelve','c')
shelf['12'] = a
shelf['ab'] = b

# 此时c,d被赋值后变成了一个Test对象.
c = shelf['12']
d = shelf['ab']

c.show()
d.show()

shelf.close()


