"""
Django URL Configuration for apps
This file maps URLs to view functions.
"""
from django.urls import path
from apps import views

app_name = 'apps'

urlpatterns = [
    # Example routes
    path('example/', views.get_example, name='get_example'),
    path('example/create/', views.create_example, name='create_example'),
    path('example/<int:id>/', views.get_example_by_id, name='get_example_by_id'),
    path('example/<int:id>/update/', views.update_example, name='update_example'),
    path('example/<int:id>/delete/', views.delete_example, name='delete_example'),
]

