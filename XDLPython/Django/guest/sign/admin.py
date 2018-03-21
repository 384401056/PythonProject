from django.contrib import admin
from sign.models import *


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'realname', 'phone', 'email', 'sign', 'create_time']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
