from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.memberships, name='memberships'),
]
