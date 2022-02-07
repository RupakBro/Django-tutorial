from django.urls import path
from . import views # 1

urlpatterns = [
    path('variables', views.display_variables),
    path('tags', views.display_tags),
    path('filters', views.display_filters),
]