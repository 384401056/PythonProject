#!/usr/bin/env python
# -*- coding utf-8 -*-

class Person:

    id = 10 # 这个字段保存在类中。称为静态字段

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('name: %s' % self.name)
        print('age: %d' % self.age)



def main():
    print(Person.__dict__)

    obj1 = Person('Lily', 20)
    obj2 = Person('Sumy', 20)

    # 此时调用的是类的静态字段
    print(obj1.id)
    print(obj2.id)
    print(obj1.__dict__)
    print(obj2.__dict__)

    # 创建了对象的字段
    obj1.id = 200
    obj2.id = 300
    print(obj1.id)
    print(obj2.id)
    print(obj1.__dict__)
    print(obj2.__dict__)

    # 显示类的静态字段
    print(Person.id)


if __name__ == '__main__':
    main()