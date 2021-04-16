from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('signup/', views.membership_signup, name='membership_signup'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('subscription_status/', views.subscription_status, name='subscription_status'),
    path('subscription_cancelled/', views.subscription_cancelled, name='subscription_cancelled'),
    path('create_subscription/', views.create_subscription,
         name='create_subscription'),
    path('wh/', webhook, name='webhook'),
]
