from django.test import TestCase
import json
from json import JSONEncoder
from datetime import datetime, date
from decimal import Decimal
# Create your tests here.

'''自定义json解析器'''
class JsonCustomEncoder(JSONEncoder):
    """自定义json解析器"""
    def default(self, field):

        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')

        # 如果是小数类型
        elif isinstance(field, Decimal):
            return str(field)
        else:
            return JSONEncoder.default(self, field)


def main():
    obj = {'obj':datetime.now()}
    print(json.dumps(obj, cls=JsonCustomEncoder))

if __name__ == '__main__':
    main()