#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import pymysql
import xlwt
import json


conn = pymysql.connect(host='220.164.82.48', port=3306, user='root', password='Flzx_3kc', db='smart', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = """
SELECT
t.Address,d.DeviceNo,d.id
FROM
  t_b_deviceinfo d,
t_s_org t
WHERE
d.OrgID = t.ID AND d.DeviceNo IN (
  '356566072694847',
  '356566072199003',
  '356566072729742',
  '356566072706245',
  '356566072706187',
  '356566072198963',
  '356566072199805',
  '356566072200009',
  '356566072781610',
  '356566072703523',
  '356566072704042',
  '356566072728264',
  '356566072705023',
  '356566072692445',
  '356566072693724',
  '356566072704109',
  '356566072695547',
  '356566072703085',
  '356566072696701',
  '356566072703200',
  '356566072701485',
  '356566072740426',
  '356566072693302',
  '356566072199482',
  '356566072692189',
  '356566072413248',
  '356566072198864',
  '356566072732985',
  '356566072694425',
  '356566072697345',
  '356566072199144',
  '356566072200728',
  '356566072706328',
  '356566072198286',
  '356566072695703',
  '356566074225061',
  '356566072035991',
  '356566072728769',
  '356566072411721',
  '356566072701089',
  '356566072697022',
  '356566072732860',
  '356566072733900',
  '356566072693161',
  '356566072696966',
  '356566072706880',
  '356566072266034',
  '356566072301906',
  '356566072693187',
  '356566072694029',
  '356566072707060',
  '356566072162696',
  '356566072730765',
  '356566072035751',
  '356566072694763',
  '356566072413180',
  '356566072454002',
  '356566072701808',
  '356566072783632',
  '356566072412067',
  '356566072727522',
  '356566072704588',
  '356566072704687',
  '356566072261951',
  '356566072705627',
  '356566072199581',
  '356566072705825',
  '356566072700164',
  '356566072415268',
  '356566072693948',
  '356566072198187',
  '356566072702525',
  '356566072704646',
  '356566072704844',
  '356566072698186',
  '356566072705684',
  '356566072702400',
  '356566072730484',
  '356566072706005',
  '356566072730286',
  '356566072683709',
  '356566072704166',
  '356566072263296',
  '356566072240153',
  '356566072742604',
  '356566072730161',
  '356566072703747',
  '356566072171846',
  '356566072738206',
  '356566072693328',
  '356566072412505',
  '356566072696180',
  '356566072268477',
  '356566072706625',
  '3566566072413248',
  '356566072690548',
  '356566072198948'
) and d.DeviceType=  2250
"""


client = pymongo.MongoClient('mongodb://220.164.82.48', 27017)
db = client['TalentCloudAgricultre']
collection = db['realdata']

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('sheet01', cell_overwrite_ok=True)  # 其中的aa是这张表的名字
sheet.write(0, 0, '地块信息')
sheet.write(0, 1, '设备编号')
sheet.write(0, 2, '设备逻辑编号')
sheet.write(0, 3, '电压值')


cursor.execute(sql)
mysqlRet = cursor.fetchall()


for index,item in enumerate(mysqlRet):
    # print(index,'---')
    ret = collection.find({"deviceid": item['id']}).limit(1).sort("date", -1)
    sheet.write(index + 1, 0, item['Address'])
    sheet.write(index + 1, 1, item['DeviceNo'])
    sheet.write(index + 1, 2, item['id'])
    try:
        sheet.write(index + 1, 3, ret[0]['value'])
    except IndexError as ex:
        print(ex)

book.save(r'C:\Users\Administrator\Desktop\xxx.xls')
















