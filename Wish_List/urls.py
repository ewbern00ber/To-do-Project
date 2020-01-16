from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/<list_id>', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('completed/<list_id>', views.completed, name='completed'),
    path('incomplete/<list_id>', views.incomplete, name='incomplete'),
    
]
