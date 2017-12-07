from datetime import datetime, date
import json

from django.test import TestCase


# Create your tests here.

class JsonCustomEncoder(json.JSONEncoder):

    def default(self, field):
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, field)




obj = {'obj':datetime.now()}
ret = json.dumps(obj, cls=JsonCustomEncoder)

print(ret)