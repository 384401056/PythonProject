from django.shortcuts import render
from django.http import *
from django.template import RequestContext, loader
from . import models
from django.db.models import F,Q,Count
import json


# Create your views here.

def  index(request):
    return HttpResponse('Django_Q')
