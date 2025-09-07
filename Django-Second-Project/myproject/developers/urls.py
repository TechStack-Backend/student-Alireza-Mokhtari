from django.urls import path
from . import views

urlpatterns = [
    path('', views.developers_list_view, name='developers_list'),
    path('<str:username>/', views.developer_cv_view, name='developer_cv'),
]
