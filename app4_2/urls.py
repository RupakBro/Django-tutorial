from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('bootstrap1', bootstrap1),
    path('bootstrap2', bootstrap2),

]