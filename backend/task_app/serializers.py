from rest_framework import serializers
from .models import *


class JobSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField()

    class Meta:
        model = Job
        fields = ('id', 'name', 'content', 'typ', 'create_time', 'status')
