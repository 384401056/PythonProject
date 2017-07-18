import sqlite3
from atexit import register

def findDataByLikeName(cursor, nameStr):
    cursor.execute("Select * From Employee Where Name like ?", ('%'+nameStr+'%',))
    # 返回一个列表
    return cursor.fetchall()

def updateData(cursor,tabName,key,val):
    cursor.execute("update %s Set %s = %f" % (tabName, key, val))
    return

def main():
    mydb = sqlite3.connect('db/employee.db')
    cur = mydb.cursor()
    resList = findDataByLikeName(cur, 'J')
    print(resList)
    cur.close()
    mydb.close()


@register
def _atexit():
    print('-----------End Line---------------')

if __name__ == '__main__':
    main()
