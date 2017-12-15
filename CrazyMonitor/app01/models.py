from django.db import models


# Create your models here.


class Host(models.Model):
    """主机"""
    name = models.CharField(max_length=64, unique=True)  # 名称唯一
    ip_addr = models.GenericIPAddressField(unique=True)  # IP地址唯一
    host_group = models.ManyToManyField('HostGroup', blank=True)  # 主机的监控模板
    templates = models.ManyToManyField('Template', blank=True)
    monitored_by_choices = (
        ('agent', 'Agent'),
        ('snmp', 'SNMP'),
        ('wget', 'WGET'),
    )
    monitored_by = models.CharField(max_length=65, choices=monitored_by_choices)  # 监控方式

    status_choices = (
        (1, 'Online'),
        (2, 'Down'),
        (3, 'Unreachable'),
        (1, 'Offline'),
    )
    status = models.IntegerField(choices=status_choices, default=1)  # 状态
    memo = models.TextField(blank=True, null=True)  # 备注

    def __str__(self):
        return '%s:%s' % (self.name, self.ip_addr)


class HostGroup(models.Model):
    """主机组"""
    name = models.CharField(max_length=64, unique=True)  # 名称唯一
    templates = models.ManyToManyField('Template', blank=True)  # 主机组的监控模板
    memo = models.TextField(blank=True, null=True)  # 备注

    def __str__(self):
        return self.name


class Service(models.Model):
    """监控服务"""
    name = models.CharField(max_length=64, unique=True)  # 名称唯一
    interval = models.IntegerField(default=60)  # 监控间隔,即多长时间上报一次数据的时间。
    plugin_name = models.CharField(max_length=64, default='n/a')  # 监控插件的名称
    items = models.ManyToManyField('ServiceIndex', verbose_name='指标列表', blank=True)  # 监控插件中的指标列表
    memo = models.TextField(blank=True, null=True)  # 备注

    def __str__(self):
        return self.name


class ServiceIndex(models.Model):
    """监控插件中的指标"""
    name = models.CharField(max_length=64)  # 名称唯一
    key = models.CharField(max_length=64)  # 实际插件中的名称，如:idle
    data_type_choices = (
        ('int', 'int'),
        ('float', 'float'),
        ('str', 'string'),
    )
    data_type = models.CharField(max_length=64, choices=data_type_choices)
    memo = models.TextField(blank=True, null=True)  # 备注

    def __str__(self):
        return "%s" % (self.name)


class Template(models.Model):
    """监控模板"""
    name = models.CharField(max_length=64, unique=True)  # 名称唯一
    # 由于Template与srvices关联，就意味着，在service中设置了interval监控间隔后，所有的使用此模板的主机，就都是一样的间隔。
    services = models.ManyToManyField('Service', verbose_name='服务列表')
    trigger = models.ManyToManyField('Trigger', verbose_name='触发器列表', blank=True)

    def __str__(self):
        return self.name


class TriggerExpression(models.Model):
    """
    触发器条件
    例如：if cpu.idle(avg(5 min)) < 80% and cpu.iowait(hit(10 min,3次)) > 50% : ....
    一个TriggerExpression只是其中的 cpu.idle(avg(5 min)) < 80% 一部分。完整的表达式，需要多条记录来组合。
    """

    # 一个触发器条件只对应一个触发器.如果反过来关联的话，一旦修改了一个条件，就会影响多个触发器了。
    trigger = models.ForeignKey('Trigger', verbose_name='所属触发器')
    service = models.ForeignKey('Service', verbose_name='关联的服务名') # 触发条件对应的服务，也就是上面表达式中的cpu等
    service_index = models.ForeignKey('ServiceIndex', verbose_name='关联的服务指标') # 触发条件对应的服务指标，也就是上面表达式中的idle,iowait等

    # 大部分服务是对应一个唯一的设备，如：CPU,MEM
    # 而有的服务是对应多个设备的。如：nic网卡，它有多个的时候，就要在此字段中指定，需要监控的是哪一个了。
    specified_index_key = models.CharField(max_length=32, verbose_name='只监控专门指定的')

    data_clac_type_choices=(
        ('avg','Average'),
        ('max','Max'),
        ('hit','Hit'),
        ('avg','Average'),
        ('last','Last'),
    )
    data_clac_func = models.CharField(choices=data_clac_type_choices, max_length=32) # 函数处理方式.
    data_clac_args = models.CharField(max_length=64, help_text='若是多个参数，用,号分开。') # 函数处理方式.
    threshold = models.IntegerField(verbose_name='阀值')

    operator_type_choices = (
        ('eq', '='),
        ('lt', '<'),
        ('gt', '>'),
    )
    # 数值判断中的大于，小于关系。
    operator_type = models.CharField(max_length=32, choices=operator_type_choices, verbose_name='运算符')


    logic_type_choices=(
        ('or','OR'),
        ('and', 'AND'),
    )
    # 表达式中的关系运算符。也就是本条记录与下一条记录的关系运算符。
    # 当进行表达式判断时。查出此表中某一个触发器对应的所有条件，顺序组合就可以执行了条件判断了。
    logic_type = models.CharField(choices=logic_type_choices, max_length=64)

    def __str__(self):
        return '%s %s (%s(%s))' % (self.service_index, self.data_clac_func, self.operator_type, self.threshold)


class Trigger(models.Model):
    """触发器"""
    name = models.CharField(max_length=64, unique=True)  # 名称唯一
    serverity_choices = (
        (1, 'Information'),
        (2, 'Warning'),
        (1, 'Average'),
        (1, 'Hight'),
        (1, 'Diaster'),
    )
    serverity = models.IntegerField(choices=serverity_choices)
    enable = models.BooleanField(default=True)
    memo = models.TextField(blank=True, null=True)  # 备注

    def __str__(self):
        return '<Trigger:%s, Serverity:%s' % (self.name, self.get_serverity_display()) # get_*_display 显示枚举类型的字段


class Action(models.Model):
    """报警"""
    name = models.CharField(max_length=64, unique=True)  # 名称唯一
    host_group = models.ManyToManyField('HostGroup', blank=True)  # 对应哪个组进行报警.
    host = models.ManyToManyField('Host', blank=True)  # 对应哪个主机进行报警.

    conditions = models.TextField() # 告警条件
    interval = models.IntegerField(default=300) # 报警间隔
    operations = models.ManyToManyField('ActionOperation')

    recover_notics = models.BooleanField(default=True) # 故障恢复，是否要进行通知。
    recover_subject = models.CharField(max_length=128, blank=True, null=True) # 通知的标题
    recover_message = models.TextField(default=True) # 通知的内容

    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ActionOperation(models.Model):
    """报警操作"""
    name = models.CharField(max_length=64)  # 名称唯一
    step = models.SmallIntegerField(default=1) # 报警次数
    action_type_choices=(
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('script', 'RunScript'),
    )
    # 报警方式，默认为发送邮件。
    action_type = models.CharField(choices=action_type_choices, default='email', max_length=32)

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    """保养计划"""
    name = models.CharField(max_length=64, unique=True)  # 名称
    host_group = models.ManyToManyField('HostGroup', blank=True)
    host = models.ManyToManyField('Host', blank=True)
    content = models.TextField('维护内容')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name















