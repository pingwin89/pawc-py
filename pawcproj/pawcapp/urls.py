# pawcapp/urls.py
from django.conf.urls import url
from django.urls import path
from pawcapp import views


urlpatterns = [
    path('', views.index, name='index'),
]