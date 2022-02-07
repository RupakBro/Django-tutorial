from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('image', views.create_image),
    path('csv', views.create_csv),
    path('pdf', views.create_pdf),
]