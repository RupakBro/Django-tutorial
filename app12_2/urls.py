from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # Create Cookie
    path('create', views.create_cookie), # Create Cookie
    path('display', views.display_cookie), # Display Cookie
]