from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import View

from Apps.Organization.models import *

# Create your views here.



class OrgListView(View):
    def get(self,request):
        return render(request, "org-list.html")
