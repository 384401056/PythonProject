from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
# Create your views here.

def index(request):
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())

    # 以上两行合为一行代码
    return  render(request, template_name='booktest/index.html')

