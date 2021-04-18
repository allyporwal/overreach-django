from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('signup/', views.membership_signup, name='membership_signup'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('membership_status/', views.membership_status,
         name='membership_status'),
    path('cancel_membership/', views.cancel_membership,
         name="cancel_membership"),
    path('membership_cancelled/', views.membership_cancelled,
         name='membership_cancelled'),
    path('create_subscription/', views.create_subscription,
         name='create_subscription'),
    path('wh/', webhook, name='webhook'),
]
