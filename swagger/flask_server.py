#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'


def main():
    app.run(host='0.0.0.0', port=8000, debug=True)


if __name__ == '__main__':
    main()
