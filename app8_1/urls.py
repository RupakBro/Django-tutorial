from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index, name='home'),
    path('display_new', views.display_new, name="display_new"),
    path('insert/', views.insert),
    path('display_edit', views.display_edit, name="edit"),
    path('update/', views.update),
    path('display_delete', views.display_delete, name="display_delete"),
    path('display_delete_confirm', views.display_delete_confirm),
    path('delete/', views.delete),

    path('model_crud', views.crud),
]