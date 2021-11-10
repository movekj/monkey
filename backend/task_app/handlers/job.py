"""
job manager
"""
from .. import models as task_models
from .. import serializers
from ...utils.exception import NotFoundError, ParamError
from ...utils import param_preprocessing


class Job:
    def __init__(self, request) -> None:
        self.requser = request.user

    def get_job(self, params) -> dict:
        params = param_preprocessing(params, filter_keys=('id', 'name', 'typ'))
        jobs = task_models.Job.objects.filter(**params).order_by('-create_time')
        data = serializers.JobSerializer(jobs, many=True).data
        return dict(data=data)

    def clean_job_data(self, data) -> dict:
        name = data.get('name')
        if not name:
            raise ParamError('name', 'name参数不能为空')

        typ = data.get('typ')
        if not typ:
            raise ParamError('typ', 'typ参数不能为空')

        content = data.get('content')
        if not content:
            raise ParamError('content', 'content参数不能为空')

        return dict(name=name, typ=typ, content=content)

    def create_job(self, data) -> dict:
        data = self.clean_job_data(data)
        name = data.get('name')

        if task_models.Job.objects.filter(name=name).exists():
            raise ParamError('name', '作业[%s]已存在' % name)

        data['status'] = 'enable'
        job = task_models.Job(**data)
        job.save()
        return dict(data=list())

    def clean_update_job_data(self, data) -> dict:
        job_id = data.get('id')
        if not job_id:
            raise ParamError('id', 'id参数不能为空')
        data = self.clean_job_data(data)
        data['id'] = job_id
        data['status'] = data.get('status', 'disable')
        return data

    def update_job(self, data) -> dict:
        job = task_models.Job.objects.filter(id=data.get('id')).first()

        if task_models.Job.objects.filter(name=data.get('name')).exclude(id=data.get('id')).exists():
            raise ParamError('id', '作业名称不能重复')

        data = self.clean_update_job_data(data)

        job.content = data.get('content')
        job.typ = data.get('typ')
        job.name = data.get('name')
        job.status = data.get('status')
        job.save()
        return dict(data='')
