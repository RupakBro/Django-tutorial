from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('about', about),
    path('serivces', services),
]