import sqlite3, os, lendydata
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

app.config.update(dict(
    DATABASE = os.path.join(app.root_path,'lendy.db'), # 数据库文件位置.
    DEBUG = True,
    SECRET_KEY = 'nickknackpaddywhack', # 保证客户端会话安全.
    USERNAME = 'admin', # 应用的证书，此处没有放在数据库中，也没有加密。
    PASSWORD = '123456'
))

app.config.from_envvar('LENDY_SETTINGS', silent=True) # 设置了一个名为LENDY_SETTINGS的环境变量为


def get_db():
    if not hasattr(g,'sqlite_db'):
        lendydata.initDB()
        g.sqlite_db = lendydata.db
        return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        lendydata.closeDB()


''' 使用修饰符来创建HTTP路由 '''
@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_inventory'))
    return render_template('login.html', error=error)

@app.route('/inventory')
def show_inventory():
    get_db()
    allItems = lendydata.get_items()
    inventory = [dict(zip(['name','description'],[item[1],item[2]])) for item in allItems]

    return render_template('items.html', items=inventory)


@app.route('/add', methods=['POST'])
def add_item():
    if not session.get('logged_in'):
        abort(401)

    lendydata.initDB()
    ownerID = [row[0] for row in lendydata.get_members()
               if row[1] == request.form['owner']]
    try:
        ownerID = ownerID[0]
    except IndexError:
        # implies no owners match name
        # should raise eror/create new member
        ownerID = 1  # use default member for now.

    lendydata.insert_item(request.form['name'],
                          request.form['description'],
                          ownerID,
                          request.form['price'],
                          request.form['condition'])

    lendydata.closeDB()

    flash('New entry was successfully posted')
    return redirect(url_for('show_inventory'))


if __name__ == '__main__':
    app.run()

