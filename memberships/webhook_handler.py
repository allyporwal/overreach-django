from django.http import HttpResponse
from profiles.models import UserProfile
from django.shortcuts import get_object_or_404


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_customer_subscription_created(self, event):
        """Assign the customer subscription id to the user's profile"""
        subscription_id = event['data']['object']['items']['data'][0]['id']
        stripe_customer_id = event['data']['object']['customer']
        profile = get_object_or_404(UserProfile, stripe_customer_id=stripe_customer_id)

        profile.stripe_subscription_id = subscription_id
        profile.save()
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
