from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('forms/new/', views.form_create, name='form_create'),
    path('forms/<int:pk>/edit/', views.form_edit, name='form_edit'),
    path('forms/<int:pk>/options/', views.option_manage, name='option_manage'),
    path('forms/<int:pk>/fill/', views.form_fill, name='form_fill'),
    path('forms/<int:pk>/analytics/', views.form_analytics, name='form_analytics'),
]
