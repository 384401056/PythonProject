#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import pymysql
import xlwt
import json
from sql_str import sql

def excelFormat(sheet):
    sheet.write(0, 0, '地块信息')
    sheet.write(0, 1, '设备编号')
    sheet.write(0, 2, '设备逻辑编号')
    sheet.write(0, 3, '电压值')


def main():
    conn = pymysql.connect(host='220.164.82.48', port=3306, user='root', password='Flzx_3kc', db='smart',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    client = pymongo.MongoClient('mongodb://220.164.82.48', 27017)
    db = client['TalentCloudAgricultre']
    collection = db['realdata']

    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('sheet01', cell_overwrite_ok=True)  # 其中的aa是这张表的名字
    excelFormat(sheet)

    cursor.execute(sql)
    mysqlRet = cursor.fetchall()

    for index, item in enumerate(mysqlRet):
        print(index, item)
        ret = collection.find({"deviceid": item['id']}).limit(1).sort("date", -1)
        sheet.write(index + 1, 0, item['Address'])
        sheet.write(index + 1, 1, item['DeviceNo'])
        sheet.write(index + 1, 2, item['id'])
        try:
            sheet.write(index + 1, 3, ret[0]['value'])
        except IndexError as ex:
            print(ex)
    book.save(r'C:\Users\Administrator\Desktop\设备数据电压统计.xls')


if __name__ == '__main__':
    main()














