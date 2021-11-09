"""
job manager
"""
from .. import models as task_models
from .. import serializers
from ...utils.exception import ParamError


class Job:
    def __init__(self, request) -> None:
        self.requser = request.user

    def get_jobs(self) -> dict:
        jobs = task_models.Job.objects.order_by('-create_time')
        data = serializers.JobSerializer(jobs, many=True).data
        return dict(data=data)

    def clean_create_job_data(self, data) -> dict:
        name = data.get('name')
        if not name:
            ParamError('name', 'name参数不能为空')

        if task_models.Job.objects.filter(name=name).exists():
            ParamError('name', '作业[%s]已存在')

        typ = data.get('typ')
        if not typ:
            ParamError('typ', 'typ参数不能为空')

        content = data.get('content')
        if not content:
            ParamError('content', 'content参数不能为空')

        return dict(name=name, typ=typ, content=content)

    def create_job(self, data) -> dict:
        data = self.clean_create_job_data(data)
        data['status'] = 'enable'
        job = task_models.Job(**data)
        job.save()
        return dict(data=list())
