from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # Create Session
    path('check_session', views.check_session), # Display Session
    path('check_session2', views.check_session2), # Display Session
]