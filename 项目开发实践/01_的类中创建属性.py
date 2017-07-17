class Circle1:

    def __init__(self,radius):
        '''初始化圆的半径'''
        self.__radius = radius

    def setRadius(self,value):
        '''设置圆的半径'''
        if value >= 0:
            self.__radius = value
        else:
            raise ValueError("半径值必须为正值.")

    def getRadius(self):
        return self.__radius

    def getArea(self):
        '''计算圆的面积'''
        return 3.1415926 * (self.__radius**2)


class Circle2:
    def __init__(self,radius):
        '''初始化圆的半径'''
        self.__radius = radius

    def __setRadius(self,value):
        '''设置圆的半径,此为内部方法'''
        if value >= 0:
            self.__radius = value
        else:
            raise ValueError("半径值必须为正值.")

    def __getRadius(self):
        return self.__radius

    # property接受一组函数，用它们来执行读、写和删除操作.
    # 此时，读操作为__getRadius方法,写操作为__setRadius方法。也就是可写不可读.
    radius = property(__getRadius,__setRadius) # 注意此处只是传入方法名

    # @property是一种创建只读属性的快捷方式
    @property
    def getArea(self): # 通过属性修饰符
        return 3.1415926 * (self.__radius ** 2)

c1 = Circle1(25.8)
print(c1.getRadius())
print('圆面积为：%.2f' % c1.getArea())
c1.setRadius(30.89)
print(c1.getRadius())
print('圆面积为：%.2f' % c1.getArea())

print("=====================================")

c2 = Circle2(25.8)
print(c2.radius)
print('圆面积为：%.2f' % c2.getArea) # 此getArea是访问只读属性.
c2.radius = 30.89
print(c2.radius)
print('圆面积为：%.2f' % c2.getArea) # 此getArea是访问只读属性.

print("=====================================")