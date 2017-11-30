#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import re


class EmailField():
    """进行Email验证的类"""

    # 验证Email的正则
    REGULAR = '^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'

    def __init__(self, error_msg_dict=None, required=True):
        """
        :param error_msg_dict: 错误提示信息字典
        :param required: 是否为必填
        """
        self.error_msg_dict = {}  # 默认错误提示
        # 如果传入错误提示信息，则用传入的。
        if error_msg_dict:
            self.error_msg_dict.update(error_msg_dict)  # update更新字典.

        self.required = required  # 是否必填
        self.is_valid = True  # 是否验证成功,默认为True
        self.value = None  # 用户输入的值
        self.name = None  # 表单中的名字
        self.error_msg = ''  # 最终的错误信息.

    def validate(self, name, input_value):
        """
        验证用户输入信息的方法
        :param name: 表单的key
        :param input_value: 用户输入
        :return:
        """
        self.name = name
        self.value = input_value

        # 如果为必填，则判断是否有值。
        if self.required:
            # 如果值为空则，设置错误信息。
            if not input_value.strip():
                self.is_valid = False
                if self.error_msg_dict.get('required', None):
                    self.error_msg = self.error_msg_dict['required']
                else:
                    self.error_msg = '%s 不能为空！' % self.name

            # 如果值不为空，则进行验证.
            else:
                val = re.match(self.REGULAR, self.value)
                # 如果验证不成功
                if not val:
                    self.is_valid = False
                    if self.error_msg_dict.get('valid', None):
                        self.error_msg = self.error_msg_dict['valid']
                    else:
                        self.error_msg = '%s 格式错误！' % self.name



class NameField():
    """进行用户名验证的类"""

    # 验证用户名的正则
    REGULAR = '^[A-Za-z0-9]+$' #　用户名正则，英文和数字

    def __init__(self, error_msg_dict=None, required=True):
        """
        :param error_msg_dict: 错误提示信息字典
        :param required: 是否为必填
        """
        self.error_msg_dict = {}  # 默认错误提示
        # 如果传入错误提示信息，则用传入的。
        if error_msg_dict:
            self.error_msg_dict.update(error_msg_dict)  # update更新字典.

        self.required = required  # 是否必填
        self.is_valid = True  # 是否验证成功,默认为True
        self.value = None  # 用户输入的值
        self.name = None  # 表单中的名字
        self.error_msg = ''  # 最终的错误信息.

    def validate(self, name, input_value):
        """
        验证用户输入信息的方法
        :param name: 表单的key
        :param input_value: 用户输入
        :return:
        """
        self.name = name
        self.value = input_value

        # 如果为必填，则判断是否有值。
        if self.required:
            # 如果值为空则，设置错误信息。
            if not input_value.strip():
                self.is_valid = False
                if self.error_msg_dict.get('required', None):
                    self.error_msg = self.error_msg_dict['required']
                else:
                    self.error_msg = '%s 不能为空！' % self.name
            # 如果值不为空，则进行验证.
            else:
                val = re.match(self.REGULAR, self.value)
                # 如果验证不成功
                if not val:
                    self.is_valid = False
                    if self.error_msg_dict.get('valid', None):
                        self.error_msg = self.error_msg_dict['valid']
                    else:
                        self.error_msg = '%s 格式错误！' % self.name


class PwdField():
    """进行密码验证的类"""

    # 验证密码的正则
    REGULAR = '^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,12}$' #　6-12位数字和字母的组合

    def __init__(self, error_msg_dict=None, required=True):
        """
        :param error_msg_dict: 错误提示信息字典
        :param required: 是否为必填
        """
        self.error_msg_dict = {}  # 默认错误提示
        # 如果传入错误提示信息，则用传入的。
        if error_msg_dict:
            self.error_msg_dict.update(error_msg_dict)  # update更新字典.

        self.required = required  # 是否必填
        self.is_valid = True  # 是否验证成功,默认为True
        self.value = None  # 用户输入的值
        self.name = None  # 表单中的名字
        self.error_msg = ''  # 最终的错误信息.

    def validate(self, name, input_value):
        """
        验证用户输入信息的方法
        :param name: 表单的key
        :param input_value: 用户输入
        :return:
        """
        self.name = name
        self.value = input_value

        # 如果为必填，则判断是否有值。
        if self.required:
            # 如果值为空则，设置错误信息。
            if not input_value.strip():
                self.is_valid = False
                if self.error_msg_dict.get('required', None):
                    self.error_msg = self.error_msg_dict['required']
                else:
                    self.error_msg = '%s 不能为空！' % self.name
            # 如果值不为空，则进行验证.
            else:
                val = re.match(self.REGULAR, self.value)
                # 如果验证不成功
                if not val:
                    self.is_valid = False
                    if self.error_msg_dict.get('valid', None):
                        self.error_msg = self.error_msg_dict['valid']
                    else:
                        self.error_msg = '%s 格式错误！' % self.name



class CheckCodeField():
    """进行验证码的验证类"""

    # 验证验证码的正则
    REGULAR = '^[0-9]{6}$' #　6位数字

    def __init__(self, error_msg_dict=None, required=True):
        """
        :param error_msg_dict: 错误提示信息字典
        :param required: 是否为必填
        """
        self.error_msg_dict = {}  # 默认错误提示
        # 如果传入错误提示信息，则用传入的。
        if error_msg_dict:
            self.error_msg_dict.update(error_msg_dict)  # update更新字典.

        self.required = required  # 是否必填
        self.is_valid = True  # 是否验证成功,默认为True
        self.value = None  # 用户输入的值
        self.name = None  # 表单中的名字
        self.error_msg = ''  # 最终的错误信息.

    def validate(self, name, input_value):
        """
        验证用户输入信息的方法
        :param name: 表单的key
        :param input_value: 用户输入
        :return:
        """
        self.name = name
        self.value = input_value

        # 如果为必填，则判断是否有值。
        if self.required:
            # 如果值为空则，设置错误信息。
            if not input_value.strip():
                self.is_valid = False
                if self.error_msg_dict.get('required', None):
                    self.error_msg = self.error_msg_dict['required']
                else:
                    self.error_msg = '%s 不能为空！' % self.name
            # 如果值不为空，则进行验证.
            else:
                val = re.match(self.REGULAR, self.value)
                # 如果验证不成功
                if not val:
                    self.is_valid = False
                    if self.error_msg_dict.get('valid', None):
                        self.error_msg = self.error_msg_dict['valid']
                    else:
                        self.error_msg = '%s 格式错误！' % self.name


def main():
    pass


if __name__ == '__main__':
    main()