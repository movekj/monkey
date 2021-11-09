from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.fields import JSONField
from rest_framework.views import APIView
from ..task_app.handlers import job
from .handlers import *


# Create your views here.

class JobView(APIView):

    def get(self, request, *args, **kwargs):
        resp = job.Job(request).get_jobs()
        return JsonResponse(resp)

    def post(self, request, *args, **kwargs):
        resp = job.Job(request).create_job(request.data)
        return JsonResponse(resp)