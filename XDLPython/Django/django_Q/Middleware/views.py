from django.http import *
from django.template import RequestContext
from django.shortcuts import *

# Create your views here.

"""自定义Rsponse,将render方法放在render中返回，这样就可以测试中间件中的process_template_response方法了"""
class Response:
    def __init__(self,request, template_name, *args, **kwargs):
        self.request = request
        self.template_name = template_name
        self.args = args
        self.kwargs = kwargs

    def render(self, *args, **kwargs):
        return render(self.request, self.template_name, *self.args, **self.kwargs)

def index(request):
    print('=====view========')
    return render(request, 'Middleware/index.html')
    # return Response(request, 'Middleware/index.html')