#!/usr/bin/env python
# -*- coding utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import time
import hashlib
import io
from PIL import Image
import os
import re

'''进行ip验证的类'''
class IPField():
    # 验证IP的正则
    REGULAR = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"

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

'''进行CheckBox的验证类'''
class CheckBoxField():

    # CheckBox不需要正则验证。
    # REGULAR = "^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$"

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
        self.is_valid = True  # 是否验证成功,默认为成功
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
            # 如果值为空,则设置错误信息
            if not input_value:
                self.is_valid = False
                if self.error_msg_dict.get('required', None):
                    self.error_msg = self.error_msg_dict['required']
                else:
                    self.error_msg = '%s 不能为空！' % self.name
            # 如果不为空.self.is_valid默认为True
        #     else:
        #         self.is_valid = True
        # else:
        #     self.is_valid = True

'''进行文件上传的验证类'''
class FileField():

    # 限制文件格式的正则表达式。
    REGULAR = "^(\w+\.jpg)|(\w+\.mp3)|(\w+\.py)$"

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
        self.value = []  # 用户输入的值,此时保存文件名列表。
        self.name = None  # 表单中的名字
        self.error_msg = ''  # 最终的错误信息.

    def validate(self, name, file_name_list):
        """
        验证用户输入信息的方法
        :param name: 表单的key
        :param file_name_list: 文件列表
        :return:
        """
        self.name = name
        self.value = file_name_list # 此时为文件列表

        # 如果为必填，则判断是否有值。
        if self.required:
            # 如果文件列表为空则，设置错误信息。
            if not file_name_list:
                self.is_valid = False
                if self.error_msg_dict.get('required', None):
                    self.error_msg = self.error_msg_dict['required']
                else:
                    self.error_msg = '%s 不能为空！' % self.name

            # 如果值不为空，则进行验证.
            else:
                for item in file_name_list:
                    val = re.match(self.REGULAR, item)
                    # 如果验证不成功
                    if not val:
                        self.is_valid = False
                        if self.error_msg_dict.get('valid', None):
                            self.error_msg = self.error_msg_dict['valid']
                        else:
                            self.error_msg = '%s 文件格式错误！' % self.name
                        break

                # val = re.match(self.REGULAR, self.value)
                # # 如果验证不成功
                # if not val:
                #     self.is_valid = False
                #     if self.error_msg_dict.get('valid', None):
                #         self.error_msg = self.error_msg_dict['valid']
                #     else:
                #         self.error_msg = '%s 格式错误！' % self.name

    def save_file(self, handler):
        # 获取文件列表.
        file_lsit = handler.request.files.get(self.name)
        file_path_name_list = []
        for item in file_lsit:
            file_path_name = os.path.join('static', 'imgs', item['filename']) # 生成路径名(含文件名)
            with open(file_path_name, 'wb') as f:
                f.write(item['body'])
            file_path_name_list.append(file_path_name)
        return file_path_name_list

'''当有多个表单的验证类时，可以将类的公共部分提取出，封装为Form表单验证的基类'''
class BaseForm:

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
            # 如果是CheckBox类型的输入
            if type(field) == CheckBoxField:
                input_value = handler.get_arguments(key)

            # 如果是file类型的输入
            elif type(field) == FileField:
                # file_list得到的是一个字典组成的列表，[{'body':'文件内容','filename':'文件名'}...]
                file_list = handler.request.files.get(key)
                file_name_list = []
                
                # 如果上传文件不为空
                if file_list:
                    for item in file_list:
                        file_name_list.append(item['filename'])  # 获取所有文件的文件名。

                input_value = file_name_list  # 将其作为inpu_value

            else:
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


'''进行Home页面Form表单验证的类'''
class HomeForm(BaseForm):
    def __init__(self):
        # 匹配ip地址
        self.ip = IPField(required=True,error_msg_dict={'required':'兄弟，别闹，IP不能为空！','valid':'哥们，看清楚，这是要输入IP..'})
        self.favor = CheckBoxField(required=True, error_msg_dict=None)
        self.loadfile = FileField(required=True, error_msg_dict=None)

class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('home.html', error_msg = None)

    def post(self, *args, **kwargs):
        obj = HomeForm()
        is_valid, success_dict, error_msg = obj.check_valid(self)
        print('is_valid: ', is_valid)
        print('success_dict: ', success_dict)
        print('error_msg: ', error_msg)
        if is_valid:
            print(obj.loadfile.save_file(self)) # 保存文件,并返回文件路径。
            self.write('post')
        else:
            self.render('home.html', error_msg = error_msg)


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
}

application = tornado.web.Application([
    (r'/home', HomeHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
