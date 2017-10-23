#!/usr/bin/env python
# -*- coding utf-8 -*-


class Person:

    def __init__(self):
        self.age = '200'


class Student(Person):

    def __init__(self):

        # 调用父类的构造方法，获取父类中封装的age
        super(Student, self).__init__()
        # Person.__init__(self) # 另一种调用父类构造方法的方法。虽然他可以单个去调用，但不推荐使用此方法。

        self.name = 'lily'


def main():
    s = Student()
    print(s.__dict__)


if __name__ == '__main__':
    main()