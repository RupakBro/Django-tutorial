from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index),
    path('display_form1', views.display_form1),
    path('get_form1/', views.get_form1),
]