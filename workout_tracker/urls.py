from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('active/', views.active_workout, name="active_workout"),
    path('delete_active_workout/', views.delete_active_workout,
         name="delete_active_workout"),
    path('log/', views.log_workout, name="log_workout"),
    path('<int:workout_id>/', views.workout, name='workout'),
    path('edit/<int:workout_id>/', views.edit_workout, name='edit_workout'),
    path('update/<int:workout_id>/',
         views.update_workout, name='update_workout'),
    path('delete/<int:workout_id>/',
         views.delete_workout, name='delete_workout'),
    path('all_workouts/', views.all_workouts, name='all_workouts'),
    path('comment/<int:workout_id>/',
         views.comment_on_workout, name='comment_on_workout'),
]
