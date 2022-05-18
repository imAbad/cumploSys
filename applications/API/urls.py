from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData.as_view(), name='apiUdis')
]
