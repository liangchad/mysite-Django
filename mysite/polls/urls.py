
# _*_coding:utf8_*_
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]