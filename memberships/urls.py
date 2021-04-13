from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.membership_signup, name='membership_signup'),
    path('checkout/', views.checkout, name='checkout'),
]
