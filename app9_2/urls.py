from django.urls import path
from . import views # 1

urlpatterns = [

    path('display_form2', views.display_form2),

]

