#!/usr/bin/env python
# -*- coding:utf-8 -*-

from backend.forms import fields



class BaseForm:
    """当有多个表单的验证类时，可以将类的公共部分提取出，封装为Form表单验证的基类"""

    def check_valid(self, handler):
        """
        检查表单提交的内容，是否符合要求。
        :param handler:
        :return:
        """
        flag = True
        success_value_dict = {}  # 成功的数据字典
        error_msg_dict = {}  # 错误信息.

        for key, field in self.__dict__.items():  # __dict__.items() 就是HomeForm类的成员变量键值对列表。
            input_value = handler.get_argument(key)

            # 通过fild对象进行表单值的验证
            field.validate(key, input_value)

            if field.is_valid:
                success_value_dict[key] = field.value
            else:
                flag = False

            # 无论是否成功，都要设置错误信息，否则前端无法取到key.成功时错误信息为''
            error_msg_dict[key] = field.error_msg

        return flag, success_value_dict, error_msg_dict


class RegForm(BaseForm):
    """进行注册页面Form表单验证的类"""
    def __init__(self):
        self.reg_name =fields.NameField(required=True,error_msg_dict={'required':'姓名不能为空！','valid':'名称格式错误，请使用英文和数字'})
        self.email = fields.EmailField(required=True,error_msg_dict={'required':'邮箱不能为空！','valid':'邮箱格式不正确！'})
        # self.checkcode = fields.CheckCodeField(required=True,error_msg_dict={'required':'验证码不能为空！','valid':'验证码格式错误'})
        self.reg_pwd = fields.PwdField(required=True,error_msg_dict={'required':'密码不能为空！','valid':'密码格式错误，请使用6-12位数字和字母的组合'})


class LoginForm(BaseForm):
    """进行登录页面Form表单验证的类"""
    def __init__(self):
        self.login_name =fields.NameField(required=True,error_msg_dict={'required':'姓名不能为空！','valid':'名称格式错误，请使用4到16位（字母，数字，下划线，减号）'})
        self.login_pwd = fields.PwdField(required=True,error_msg_dict={'required':'密码不能为空！','valid':'密码格式错误，请使用6-12位数字和字母的组合'})


def main():
    pass


if __name__ == '__main__':
    main()