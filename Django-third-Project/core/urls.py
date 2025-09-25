from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('developers/', views.developers_list, name='developers_list'),
    path('developers/new/', views.developer_create, name='developer_create'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/new/', views.project_create, name='project_create'),
]
