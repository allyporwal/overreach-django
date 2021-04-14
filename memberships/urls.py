from django.urls import path, include
from . import views
from .webhooks import webhook_received

urlpatterns = [
    path('signup/', views.membership_signup, name='membership_signup'),
    path('checkout/', views.checkout, name='checkout'),
    path('wh/', webhook_received, name='webhook_received'),
]
