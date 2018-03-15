#!/usr/bin/env python
# -*- coding utf-8 -*-
import tornado.ioloop
import tornado.web
import template_func as tfn
import template_modules as tfm

# 全局变量，存储用户列表.
USER_LIST = []


class MainHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument('name')
        # 如果没有参数就不添加
        if username != '':
            USER_LIST.append(username)
        self.render('s1.html', title='This is title', user_list=USER_LIST)

    def get(self, *args, **kwargs):
        self.render('s1.html', title='This is title', user_list=USER_LIST)


settings = {
    'template_path': 'static',
    'static_path': 'static',  # 静态资源的路径
    'static_url_prefix': '/static/',  # 静态资源的前缀
    'ui_methods': tfn,  # 定义ui的函数模块
    'ui_modules':tfm,  # 定义ui的模型
}

'''
Tornado内部提供的函数、字段、类以供html模板使用：
escape: tornado.escape.xhtml_escape 的別名
xhtml_escape: tornado.escape.xhtml_escape 的別名
url_escape: tornado.escape.url_escape 的別名
json_encode: tornado.escape.json_encode 的別名
squeeze: tornado.escape.squeeze 的別名
linkify: tornado.escape.linkify 的別名
datetime: Python 的 datetime 模组
handler: 当前的 RequestHandler 对象
request: handler.request 的別名
current_user: handler.current_user 的別名
locale: handler.locale 的別名
_: handler.locale.translate 的別名
static_url: for handler.static_url 的別名
xsrf_form_html: handler.xsrf_form_html 的別名
'''

application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
