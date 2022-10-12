from django.urls import path

from . import views 

# /api/products/
urlpatterns = [
    path('', views.task_list_create_view, name='task-list'),
    path('<int:pk>/update/', views.task_update_view, name='task-update'),
    path('<int:pk>/destroy/', views.task_destroy_view, name='task-destroy'),
]