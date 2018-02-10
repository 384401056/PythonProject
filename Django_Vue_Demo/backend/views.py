from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    ret = {}
    ret['name'] = 'Jims'
    ret['age'] = 10
    return JsonResponse(ret)