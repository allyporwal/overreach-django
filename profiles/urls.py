from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:profile_id>/', views.profile, name="profile"),
    path('edit/', views.edit_profile, name="edit_profile"),
    path('follow/<int:profile_id>', views.add_follower, name="add_follower"),
]
