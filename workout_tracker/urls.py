from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.workout_tracker, name="workout_tracker"),
]
