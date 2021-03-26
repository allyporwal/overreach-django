from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.log_workout, name="log_workout"),
    path('<int:workout_id>/', views.workout, name='workout'),
]
