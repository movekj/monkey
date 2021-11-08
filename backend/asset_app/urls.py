
from django.urls import path
from . import views
from django.views import View


urlpatterns = [
    path('index/', views.index),
]
