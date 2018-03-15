import pymysql
# Django默认的链接mysql用的是MySQLdb模块，但此模块没有python3.x的版本，所以要用pymysql模块替换MySQLdb模块
pymysql.install_as_MySQLdb()