from django.urls import path
from . import views

urlpatterns = [
    path('', views.personnel_list, name='personnel_list'), 
    path('create/', views.personnel_create, name='personnel_create'), 
    path('update/<int:pk>/', views.personnel_update, name='personnel_update'), 
    path('delete/<int:pk>/', views.personnel_delete, name='personnel_delete'), 
    path('data/', views.personnel_data, name='personnel_data'), 
    path('register/', views.register, name='register'), 
]
