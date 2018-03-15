from django.contrib import admin
from app01 import models


# Register your models here.


class HostAdmin(admin.ModelAdmin):
    # 设置列表视图
    list_display = ('id', 'name', 'ip_addr', 'status')

class HostGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class TemplateAdmin(admin.ModelAdmin):
    filter_horizontal = ('services', 'trigger')

class ServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)
    list_display = ('id', 'name', 'interval', 'plugin_name')

class TriggerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serverity', 'enable')

class TriggerExpressionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'trigger',
        'service',
        'specified_index_key',
        'data_clac_func',
        'threshold',
        'operator_type',
        'logic_type'
    )


admin.site.register(models.Action)
admin.site.register(models.ActionOperation)
admin.site.register(models.Host, HostAdmin)
admin.site.register(models.HostGroup, HostGroupAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.ServiceIndex)
admin.site.register(models.Template, TemplateAdmin)
admin.site.register(models.Trigger, TriggerAdmin)
admin.site.register(models.TriggerExpression, TriggerExpressionAdmin)
admin.site.register(models.Maintenance)
