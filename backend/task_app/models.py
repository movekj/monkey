from django.db import models

# Create your models here.


class Job(models.Model):
    TYP_CHOICES = (
        ('scrpit', '脚本'),
        ('playbook', 'ansible playbook')
    )
    STATUS_CHOICES = (
        ('online', '上线'),
        ('offline', '下线')
    )
    name = models.CharField(verbose_name='作业名称', max_length=20)
    content = models.TextField(verbose_name='作业内容')
    typ = models.CharField(choices=TYP_CHOICES, verbose_name='脚本类型', max_length=30)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, verbose_name='状态', max_length=20)

    class Meta:
        verbose_name = 'Job'

    def __str__(self):
        return str(self.name)

class JobHistory(models.Model):
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now_add=True)
    content = models.TextField(verbose_name='作业内容')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Job_History'

    def __str__(self):
        return str(self.job)

class Task(models.Model):
    EXEC_MODE_CHOICES = (
        ('serial', '串行'),
        ('parallel', '并行')
    )
    start_time = models.DateTimeField(verbose_name='开始时间', auto_now_add=True)
    end_time = models.DateTimeField(verbose_name='结束时间', null=True)
    hosts = models.JSONField(verbose_name='目标主机列表')
    output = models.JSONField(verbose_name='任务输出', null=True)
    jobs = models.JSONField(verbose_name='任务执行的作业列表')
    exec_mode = models.CharField(choices=EXEC_MODE_CHOICES, verbose_name='作业执行方式', max_length=30)

    class Meta:
        verbose_name = 'Task'

    def __str__(self):
        return str(self.jobs)
