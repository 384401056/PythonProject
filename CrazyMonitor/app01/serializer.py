#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app01 import models


class ClientHandler(object):

    def __init__(self, client_id):
        self.client_id = client_id
        self.client_configs = {
            'services': {}
        }

    def fech_configs(self):
        """
        获取配置数据
        :return:
        """
        try:
            host_obj = models.Host.objects.get(id=self.client_id)  # 根据ID获取主机
            templates_list = list(host_obj.templates.select_related())  # 根据主机获取模板列表
            # print('host_obj_template:', templates_list)

            host_group = list(host_obj.host_group.select_related())  # 根据主机获取主机组
            for host in host_group:  # 再根据主机组获取主机和其中的templates，加入templates_list
                templates_list.extend(host.templates.select_related())
            # 最终templates_list中可能会有重复的templates
            # print('host_all_template:', templates_list)

            for template in templates_list:
                # 循环temlate中的services,组装client_configs字典
                for services in list(template.services.select_related()):
                    # 返回插件名和间隔,此时就会自动把重复的template中的services去重。最终返回的只是services
                    self.client_configs['services'][services.name] = [services.plugin_name, services.interval]
        except Exception as ex:
            print(ex)

        return self.client_configs

    def get_host_trgger(self, host_obj):
        """获取主机的触发器"""
        triggers = []
        for tem in host_obj.templates.select_related():
            triggers.append(tem.trigger.select_related())

        for group in host_obj.host_group.select_related():
            for tem in group.templates.select_related():
                triggers.append(tem.trigger.select_related())

        return set(triggers)

def main():
    pass


if __name__ == '__main__':
    main()
