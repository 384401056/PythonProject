import shelve
import json
from datetime import datetime
from flask import Flask, request, redirect, escape, Markup
from flask_cors import *  # 解决跨域问题

application = Flask(__name__)
CORS(application, supports_credentials=True) # 解决跨域问题

DATA_FILE = 'guestbook.dat'

def save_data(name, comment, create_at):
    ''' 保存提交的数据 '''
    database = shelve.open(DATA_FILE)
    # 如果数据库中没有greeting_list则新建
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']
    # 插入数据在列表的首部
    greeting_list.insert(0, {'name':name, 'comment':comment, 'create_at':create_at})
    database['greeting_list'] = greeting_list
    database.close()

def load_data():
    '''返回已经提交后的数据'''
    database = shelve.open(DATA_FILE)
    greeting_list = database.get('greeting_list', [])
    database.close()
    jsonStr = json.dumps({"dataList":greeting_list})
    return jsonStr




""" 路由 """
@application.route('/')
def index():
    ''' 当访问首页时调用的方法 '''
    return load_data()


@application.route('/post', methods=['POST'])
def post():
    ''' 用于提交评论 '''
    postForm = request.form
    getArgs = request.args
    postValues = request.values
    re = request
    name = request.values.get('name')
    comment = request.values.get('comment')
    create_at = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    # print("name:"+ name)
    # print("comment:"+ comment)
    # print("create_at:"+ create_at)
    # 存储数据
    # save_data(name,comment,create_at)
    # 重定向至首页
    # return redirect('/')
    return "OK"



""" 模版过滤器 """
@application.template_filter('nl2br')
def nl2br_fillter(s):
    """将换行符转换为<br>"""
    return escape(s).replace('\n', Markup('<br>'))

@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    return dt.strftime('%Y/%m/%d %H:%M:%S')


if __name__ == '__main__':
    application.run('127.0.0.1', 8000, debug=True)