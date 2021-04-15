from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('signup/', views.membership_signup, name='membership_signup'),
    path('checkout/', views.checkout, name='checkout'),
    path('create_subscription/', views.create_subscription,
         name='create_subscription'),
    path('wh/', webhook, name='webhook'),
]
