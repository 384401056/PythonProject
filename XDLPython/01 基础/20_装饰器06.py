#!/usr/bin/env python
# -*- coding: utf-8 -*-


class User(object):
    def __init__(self, roles):
        self.roles = roles


def myprotect(role):
    def outer(function):
        def wrapper(*args, **kwargs):
            # global user
            user = globals().get('user') # 作用与上一句相同，使用全局变量。

            # 如果用户没admin权限，则返回None，否则执行原函数。
            if user is None or role not in user.roles:
                # raise Exception("You don't have authority!") # 或者直接抛异常，就不用返回None了
                print("You don't have authority!")
                return None

            return function(*args, **kwargs)

        return wrapper
    return outer


class MyMethods(object):
    @myprotect('admin')
    def mylogin(self):
        """
        通过装饰器装饰后，只有拥用admin权限的user才能调用此方法。
        :return:
        """
        print("Login")


#创建一个全局用户对象，并设置其权限为 admin user
# user = User(('admin', 'user'))
user = User(('user'))


def main():
    myInvoke = MyMethods()
    myInvoke.mylogin()

if __name__ == '__main__':
    main()
