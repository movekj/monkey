from django.urls.conf import include
from django.urls import path
from .views import *

urlpatterns = [
    path('job/', JobView.as_view()),
]
