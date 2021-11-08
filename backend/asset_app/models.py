from django.db import models

# Create your models here.

class Host(models.Model):
    STATUS_CHOICE = (
        ('enable', '启用'),
        ('disable', '禁用')
    )
    address = models.CharField(max_length=120, verbose_name='主机链接地址')
    manage_port = models.CharField(max_length=10, verbose_name='管理端口')
    hostname = models.CharField(max_length=200, verbose_name='主机名')
    remark = models.CharField(max_length=512, verbose_name='备注')
    status = models.CharField(max_length=40, choices=STATUS_CHOICE, verbose_name='状态')
    tag = models.CharField(max_length=30, verbose_name='标签')

    class Meta:
        verbose_name = 'Host'

    def __str__(self):
        return str(self.hostname)

class Group(models.Model):
    name = models.CharField(max_length=80, verbose_name='名称')

    class Meta:
        verbose_name = 'Group'

    def __str__(self):
        return str(self.name)

class Host_Group(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Host_Group'

    def __str__(self):
        return str(self.host) + '-' + str(self.group)
