from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('display_form1', display_form1),
    path('get_values1', get_values1),
    path('get_values2', get_values2),
]