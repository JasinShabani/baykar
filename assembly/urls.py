from django.urls import path
from . import views

urlpatterns = [
    path('assemble/', views.assemble_plane, name='assemble_plane'),  
    
    path('success/', views.assembly_success, name='assembly_success'),
    
    path('assembly/rapor/', views.assembly_report, name='assembly_report'),
]
