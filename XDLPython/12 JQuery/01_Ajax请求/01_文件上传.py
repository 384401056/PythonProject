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



IMG_LIST = []


class BaseHandle(tornado.web.RequestHandler):
    '''
    创建一个公共的父类，初始化时创建session.(RequestHandler原码中的initialize方法是在__init__方法最后执行的。)
    这样的话，在IndexHandler，ManagerHandler中就不用创建Session对象了。
    '''
    def initialize(self):
        pass


class UpLoadHandler(BaseHandle):
    '''普通文件上传'''
    def get(self, *args, **kwargs):
        self.render('upLoad.html', img_list=IMG_LIST)

    def post(self, *args, **kwargs):
        print(self.get_argument('name'))
        print(self.get_arguments('faver'))

        # 获取上传文件.
        file_metas = self.request.files['fname']
        for meta in file_metas:
            img_name = meta['filename'] # 获取文件名称

            # 指定文件路径，并保存图片
            new_img_file = os.path.join('static', 'imgs', img_name)
            with open(new_img_file, 'wb') as f:
                f.write(meta['body'])

        IMG_LIST.append(new_img_file)
        self.redirect('/upLoad') # 此语句在Ajax上传文件时，无效.


        # 显示图片
        # im = Image.open(img_name)
        # msstream = io.BytesIO()
        # im.save(msstream, "jpeg")
        # im.close()
        # self.set_header('Content-Type', 'image/jpg')  # 设置头类型
        # self.write(msstream.getvalue())  # 返回IO流中的数据。


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
}

application = tornado.web.Application([
    (r'/upLoad', UpLoadHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
