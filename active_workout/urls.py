from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.active_workout, name="active_workout"),
    path('delete_active_workout/', views.delete_active_workout,
         name="delete_active_workout"),
]
