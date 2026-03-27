from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_contact, name='add'),
    path('edit/<int:id>/', views.edit_contact, name='edit'),
    path('delete/<int:id>/', views.delete_contact, name='delete'),
]
