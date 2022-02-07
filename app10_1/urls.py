from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPersons.as_view(), name='persons'), # Display All Persons
    path('person/', views.PersonCreate.as_view()), # Insert New Person
    path('person/details/<int:pk>', views.PersonDetail.as_view()), # Display Details of Individual Person
    path('person/update/<int:pk>', views.PersonUpdate.as_view()), # Edit Person
    path('person/delete/<int:pk>', views.PersonDelete.as_view()), # Delete Person
]