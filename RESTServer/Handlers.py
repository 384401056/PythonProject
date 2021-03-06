#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import json


class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Content-Type', 'application/json;charset=UTF-8')


class QueryParcel(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        ret = {
            "data": [
                {
                    "addresscode": 530111002002,
                    "addressdetail": "佛挡杀佛要",
                    "addressfullname": "云南省昆明市官渡区太和街道办事处永胜路社区居委会佛挡杀佛要",
                    "area": 30,
                    "belongpeasant": {
                        "addresscode": 110101001001,
                        "addressdetail": "呵呵小组",
                        "birthday": "2018-01-03 00:00:00",
                        "cooperstate": "cooper-underway",
                        "creattime": "2018-01-28 16:18:17",
                        "culture": "culture-doctor",
                        "delstate": 1,
                        "edittime": "2018-02-12 10:26:05",
                        "explain": "群殴第三季度撒角度看",
                        "id": 5,
                        "identity": "531211111111111110",
                        "ispoverty": "poverty-yes",
                        "linkphone": "158888883488",
                        "name": "测试农户9999",
                        "orgid": 1,
                        "pid": "NH0005",
                        "sex": "sex-man"
                    },
                    "belongpeasantid": 5,
                    "creattime": "2018-02-26 15:32:52",
                    "delstate": 1,
                    "departmentid": 3,
                    "departmentname": "研发部二部",
                    "dependenceid": "parcel-self",
                    "dependencename": "自营",
                    "edittime": "2018-02-26 15:32:52",
                    "elevation": 20,
                    "id": 5,
                    "name": "老王测试4",
                    "parcelno": "530111002002-101",
                    "responsibleuser": [
                        {
                            "addresscode": 530113000000,
                            "addressdetail": "西山区科技园",
                            "birthday": "1986-12-12 00:00:00",
                            "creattime": "2018-02-10 16:42:55",
                            "delstate": 1,
                            "edittime": "2018-02-12 10:22:34",
                            "email": "371557412@qq.com",
                            "id": 31,
                            "jobnumber": "xx002123",
                            "loginorgid": 1,
                            "name": "鱼德华31",
                            "nickname": "鱼摆摆",
                            "parcelid": 5,
                            "password": "6ZoYxCjLONXyYIU2eJIuAw==",
                            "phone": "15288121873",
                            "photo": 575,
                            "sex": "1",
                            "status": "1",
                            "userid": 31
                        },
                        {
                            "addresscode": 530113000000,
                            "addressdetail": "西山区科技园",
                            "birthday": "1986-12-12 00:00:00",
                            "creattime": "2018-02-11 11:16:34",
                            "delstate": 1,
                            "edittime": "2018-02-12 10:22:34",
                            "email": "371557412@qq.com",
                            "id": 36,
                            "jobnumber": "xx0021112",
                            "loginorgid": 1,
                            "name": "鱼德华36",
                            "nickname": "鱼摆摆",
                            "parcelid": 5,
                            "password": "6ZoYxCjLONXyYIU2eJIuAw==",
                            "phone": "15288121878",
                            "photo": 582,
                            "sex": "1",
                            "status": "1",
                            "userid": 36
                        }
                    ],
                    "responsibleusername": "鱼德华31,鱼德华36"
                },
                {
                    "addresscode": 530103001002,
                    "addressdetail": "老王测试3",
                    "addressfullname": "云南省昆明市盘龙区拓东街道办事处明通社区居委会老王测试3",
                    "area": 10,
                    "belongpeasant": {
                        "addresscode": 110101001001,
                        "addressdetail": "呵呵小组",
                        "birthday": "2018-01-03 00:00:00",
                        "cooperstate": "cooper-underway",
                        "creattime": "2018-01-28 16:18:17",
                        "culture": "culture-doctor",
                        "delstate": 1,
                        "edittime": "2018-02-12 10:26:05",
                        "explain": "群殴第三季度撒角度看",
                        "id": 5,
                        "identity": "531211111111111110",
                        "ispoverty": "poverty-yes",
                        "linkphone": "158888883488",
                        "name": "测试农户9999",
                        "orgid": 1,
                        "pid": "NH0005",
                        "sex": "sex-man"
                    },
                    "belongpeasantid": 5,
                    "creattime": "2018-02-26 15:32:04",
                    "delstate": 1,
                    "departmentid": 38,
                    "departmentname": "4",
                    "dependenceid": "parcel-cooper",
                    "dependencename": "合作",
                    "edittime": "2018-02-26 15:32:04",
                    "elevation": 100,
                    "id": 4,
                    "name": "老王测试3",
                    "parcelno": "530103001002-102",
                    "responsibleuser": []
                },
                {
                    "addresscode": 530103001001,
                    "addressdetail": "老王测试2",
                    "addressfullname": "云南省昆明市盘龙区拓东街道办事处尚义社区居委会老王测试2",
                    "area": 1,
                    "belongpeasant": {
                        "addresscode": 130102001001,
                        "addressdetail": "某个嘎啦里面",
                        "birthday": "2018-01-26 00:00:00",
                        "cooperstate": "cooper-nostart",
                        "creattime": "2018-01-26 10:44:20",
                        "culture": "culture-underprimary",
                        "delstate": 1,
                        "edittime": "2018-02-12 10:26:05",
                        "explain": "爱抽烟喝酒等说明",
                        "id": 4,
                        "identity": "531211111111111119",
                        "ispoverty": "poverty-yes",
                        "linkphone": "15888888885",
                        "name": "2测试用户111",
                        "orgid": 1,
                        "pid": "NH0004",
                        "sex": "sex-woman"
                    },
                    "belongpeasantid": 4,
                    "creattime": "2018-02-26 15:29:26",
                    "delstate": 1,
                    "departmentid": 1,
                    "departmentname": "产品市场部",
                    "dependenceid": "parcel-cooper",
                    "dependencename": "合作",
                    "edittime": "2018-02-26 15:29:26",
                    "elevation": 2,
                    "id": 3,
                    "name": "老王测试2",
                    "parcelno": "530103001001-103",
                    "responsibleuser": [
                        {
                            "addresscode": 530113000000,
                            "addressdetail": "西山区科技园",
                            "birthday": "1986-12-12 00:00:00",
                            "creattime": "2018-02-10 16:42:55",
                            "delstate": 1,
                            "edittime": "2018-02-12 10:22:34",
                            "email": "371557412@qq.com",
                            "id": 31,
                            "jobnumber": "xx002123",
                            "loginorgid": 1,
                            "name": "鱼德华31",
                            "nickname": "鱼摆摆",
                            "parcelid": 3,
                            "password": "6ZoYxCjLONXyYIU2eJIuAw==",
                            "phone": "15288121873",
                            "photo": 575,
                            "sex": "1",
                            "status": "1",
                            "userid": 31
                        },
                        {
                            "addresscode": 530113000000,
                            "addressdetail": "西山区科技园",
                            "birthday": "1986-12-12 00:00:00",
                            "creattime": "2018-02-11 11:16:34",
                            "delstate": 1,
                            "edittime": "2018-02-12 10:22:34",
                            "email": "371557412@qq.com",
                            "id": 36,
                            "jobnumber": "xx0021112",
                            "loginorgid": 1,
                            "name": "鱼德华36",
                            "nickname": "鱼摆摆",
                            "parcelid": 3,
                            "password": "6ZoYxCjLONXyYIU2eJIuAw==",
                            "phone": "15288121878",
                            "photo": 582,
                            "sex": "1",
                            "status": "1",
                            "userid": 36
                        }
                    ],
                    "responsibleusername": "鱼德华31,鱼德华36"
                },
                {
                    "addresscode": 530102001001,
                    "addressdetail": "老王测试1",
                    "addressfullname": "云南省昆明市五华区华山街道办事处翠湖西路社区老王测试1",
                    "area": 1,
                    "belongpeasant": {
                        "addresscode": 110101001001,
                        "addressdetail": "呵呵小组",
                        "birthday": "2018-01-03 00:00:00",
                        "cooperstate": "cooper-underway",
                        "creattime": "2018-01-28 16:18:17",
                        "culture": "culture-doctor",
                        "delstate": 1,
                        "edittime": "2018-02-12 10:26:05",
                        "explain": "群殴第三季度撒角度看",
                        "id": 5,
                        "identity": "531211111111111110",
                        "ispoverty": "poverty-yes",
                        "linkphone": "158888883488",
                        "name": "测试农户9999",
                        "orgid": 1,
                        "pid": "NH0005",
                        "sex": "sex-man"
                    },
                    "belongpeasantid": 5,
                    "creattime": "2018-02-26 15:28:16",
                    "delstate": 1,
                    "departmentid": 4,
                    "departmentname": "销售运营部",
                    "dependenceid": "parcel-self",
                    "dependencename": "自营",
                    "edittime": "2018-02-26 15:28:16",
                    "elevation": 1,
                    "id": 2,
                    "name": "老王测试1",
                    "parcelno": "530102001001-104",
                    "responsibleuser": [
                        {
                            "addresscode": 530113000000,
                            "addressdetail": "西山区科技园",
                            "birthday": "1986-12-12 00:00:00",
                            "creattime": "2018-02-11 11:04:31",
                            "delstate": 1,
                            "edittime": "2018-02-12 10:22:34",
                            "email": "371557412@qq.com",
                            "id": 33,
                            "jobnumber": "xx002",
                            "name": "鱼德华33",
                            "nickname": "鱼摆摆",
                            "parcelid": 2,
                            "password": "6ZoYxCjLONXyYIU2eJIuAw==",
                            "phone": "15288121875",
                            "photo": 579,
                            "sex": "1",
                            "status": "1",
                            "userid": 33
                        }
                    ],
                    "responsibleusername": "鱼德华33"
                },
                {
                    "addresscode": 530102001001,
                    "addressdetail": "测试基地",
                    "addressfullname": "云南省昆明市五华区华山街道办事处翠湖西路社区测试基地",
                    "area": 1,
                    "belongpeasant": {
                        "addresscode": 130102001001,
                        "addressdetail": "某个嘎啦里面",
                        "birthday": "2018-01-26 00:00:00",
                        "cooperstate": "cooper-nostart",
                        "creattime": "2018-01-26 10:44:20",
                        "culture": "culture-underprimary",
                        "delstate": 1,
                        "edittime": "2018-02-12 10:26:05",
                        "explain": "爱抽烟喝酒等说明",
                        "id": 4,
                        "identity": "531211111111111119",
                        "ispoverty": "poverty-yes",
                        "linkphone": "15888888885",
                        "name": "2测试用户111",
                        "orgid": 1,
                        "pid": "NH0004",
                        "sex": "sex-woman"
                    },
                    "belongpeasantid": 4,
                    "creattime": "2018-02-25 09:39:55",
                    "delstate": 1,
                    "departmentid": 3,
                    "departmentname": "研发部二部",
                    "dependenceid": "parcel-self",
                    "dependencename": "自营",
                    "edittime": "2018-02-25 09:39:55",
                    "elevation": 1,
                    "id": 1,
                    "introduce": "",
                    "name": "昆明测试地块2",
                    "parcelno": "530102001001-105",
                    "parceltypeid": "1,2,4,3,4",
                    "responsibleuser": [
                        {
                            "addresscode": 530113000000,
                            "addressdetail": "西山区科技园",
                            "birthday": "1986-12-12 00:00:00",
                            "creattime": "2018-02-10 16:42:55",
                            "delstate": 1,
                            "edittime": "2018-02-12 10:22:34",
                            "email": "371557412@qq.com",
                            "id": 31,
                            "jobnumber": "xx002123",
                            "loginorgid": 1,
                            "name": "鱼德华31",
                            "nickname": "鱼摆摆",
                            "parcelid": 1,
                            "password": "6ZoYxCjLONXyYIU2eJIuAw==",
                            "phone": "15288121873",
                            "photo": 575,
                            "sex": "1",
                            "status": "1",
                            "userid": 31
                        },
                        {
                            "addresscode": 530113000000,
                            "addressdetail": "西山区科技园",
                            "birthday": "1986-12-12 00:00:00",
                            "creattime": "2018-02-11 11:16:34",
                            "delstate": 1,
                            "edittime": "2018-02-12 10:22:34",
                            "email": "371557412@qq.com",
                            "id": 36,
                            "jobnumber": "xx0021112",
                            "loginorgid": 1,
                            "name": "鱼德华36",
                            "nickname": "鱼摆摆",
                            "parcelid": 1,
                            "password": "6ZoYxCjLONXyYIU2eJIuAw==",
                            "phone": "15288121878",
                            "photo": 582,
                            "sex": "1",
                            "status": "1",
                            "userid": 36
                        }
                    ],
                    "responsibleusername": "鱼德华31,鱼德华36"
                }
            ],
            "flag": 1,
            "message": "操作成功",
            "servicecurrenttime": "2018-02-28 17:51:47"
        }
        self.write(json.dumps(ret))


class KnowledgeContent(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        print(self.get_argument('content_id'))
        print(self.get_argument('user_Id'))
        ret = {
            "data": {
                "title": "什么是三七涝害？如何预防？",
                "release_date": 1497499552000,
                "author": "余大朝",
                "up_num": 0,
                "txt": "<p style=\"text-indent: 0px; background: white; vertical-align: top; line-height: 1.75em; margin-bottom: 10px; margin-top: 10px;\"><span style=\"font-size: 15px;font-family: 微软雅黑, sans-serif;letter-spacing: 1px\">答：势低凹易积水或过于平坦、排水不畅的七园，由于土壤中水分过多造成氧气供应不足，使三七植株的根部呼吸受阻而致病的现象就是三七涝害。受害植株根部呈褐色并腐烂，地上部则表现叶片变黄、落叶、落花等症状。该病害与病原侵染引起的根褐腐病极为相似，所不同的是后者经镜检或培养可见多种病原，而该病经镜检或微生物培养不能发现病原。</span></p><p style=\"text-indent: 0px; background: white; vertical-align: top; text-align: center; line-height: 1.75em; margin-bottom: 10px; margin-top: 10px;\"><span style=\"font-size: 15px;font-family: 微软雅黑, sans-serif;letter-spacing: 1px\"><img src=\"/resources/sgsq_cms/u/cms/www/201706/15120548q7y6.jpg\" title=\"9.jpg\" alt=\"9.jpg\" width=\"720\" height=\"480\"/></span></p><p style=\"text-indent: 0px; background: white; vertical-align: top; line-height: 1.75em; margin-bottom: 10px; margin-top: 10px;\"><span style=\"font-size: 15px;font-family: 微软雅黑, sans-serif;letter-spacing: 1px\">选地种植三七时应避开凹地或不易排水的平地；若已选用平地，应深开沟，理高墒，避免积水引起病害的发生。</span></p>",
                "ups": "0",
                "collection": 0,
                "thumbsUp": 0,
                "comments": 1
            }
        }
        self.write(json.dumps(ret))


class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.write(json.dumps(({"name": "gaoyanbin", "age": 2000})))

    def post(self, *args, **kwargs):
        # 当post的请求头是application/x-www-form-urlencoded时，用以下方法接收数据。
        # param1 = self.get_argument('age')
        # param2 = self.get_argument('username')
        # print(param1)
        # print(param2)

        # 当post的请求头是application/json时，用以下方法接收数据。
        # param = self.request.body.decode('utf-8')
        # param = json.loads(param)
        # print(param)

        self.write(json.dumps({"status": "OK"}))
