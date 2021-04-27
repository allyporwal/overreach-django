from django.http import HttpResponse
from profiles.models import UserProfile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime
from django.utils.timezone import make_aware


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_welcome_email(self, email_data):
        """send the user a welcome email when their subscription
        has been created"""
        user_email = email_data.email
        subject = render_to_string(
            'memberships/welcome_emails/welcome_email_subject.txt',
            {'email_data': email_data})
        body = render_to_string(
            'memberships/welcome_emails/welcome_email_body.txt',
            {'email_data': email_data,
             'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(subject,
                  body,
                  settings.DEFAULT_FROM_EMAIL,
                  [user_email]
                  )

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_customer_subscription_created(self, event):
        """Assign the customer subscription id to the user's profile"""
        subscription_id = (event['data']['object']
                           ['items']['data'][0]['subscription'])
        stripe_customer_id = event['data']['object']['customer']

        try:
            profile = UserProfile.objects.get(
                stripe_customer_id=stripe_customer_id)
            profile.stripe_subscription_id = subscription_id
            profile.save()
            # data for email send
            first_name = profile.first_name
            email = profile.default_billing_email
            email_data = {
                'first_name': first_name,
                'email': email,
                'subscription_id': subscription_id,
            }
            self._send_welcome_email(email_data)

            return HttpResponse(
                content=f'Webhook received: {event["type"]}.\
                    UserProfile subscribed', status=200)

        except UserProfile.DoesNotExist:
            return HttpResponse(
                content=f'Webhook received: {event["type"]}.\
                    UserProfile does not exist.', status=404)

    def handle_customer_subscription_deleted(self, event):
        """Cancel subscription on user's profile and revoke access"""
        subscription_id = event['data']['object']['id']
        stripe_customer_id = event['data']['object']['customer']

        try:
            profile = UserProfile.objects.get(
                stripe_customer_id=stripe_customer_id)
            # first_name = profile.first_name
            # email = profile.default_billing_email
            # email_data = {
            #     'first_name': first_name,
            #     'email': email,
            #     'subscription_id': subscription_id,
            # }
            profile.is_subscribed = False
            profile.stripe_subscription_id = f'Cancelled {subscription_id}'
            profile.save()
            return HttpResponse(
                content=f'Webhook received: {event["type"]}.\
                    Subscription deleted', status=200)

        except UserProfile.DoesNotExist:
            return HttpResponse(
                content=f'Webhook received: {event["type"]}.\
                    UserProfile does not exist.', status=404)

    def handle_invoice_payment_failed(self, event):
        """Suspend user's access and contact them if payment fails"""
        stripe_customer_id = event['data']['object']['customer']

        try:
            profile = UserProfile.objects.get(
                stripe_customer_id=stripe_customer_id)
            profile.is_subscribed = False
            profile.save()
            return HttpResponse(
                content=f'Webhook received: {event["type"]}.\
                    UserProfile access suspended', status=200)

        except UserProfile.DoesNotExist:
            return HttpResponse(
                content=f'Webhook received: {event["type"]}.\
                    UserProfile does not exist.', status=404)

    def handle_invoice_payment_succeeded(self, event):
        """Update subscription information for the user"""
        stripe_customer_id = event['data']['object']['customer']
        last_payment_unix = (event['data']['object']['lines']
                             ['data'][0]['period']['start'])
        next_payment_unix = (event['data']['object']['lines']
                             ['data'][0]['period']['end'])

        # convert timestamp to timezone aware datetime
        last_payment = make_aware(datetime.fromtimestamp(last_payment_unix))
        next_payment = make_aware(datetime.fromtimestamp(next_payment_unix))

        try:
            profile = UserProfile.objects.get(
                stripe_customer_id=stripe_customer_id)
            profile.last_payment = last_payment
            profile.next_payment = next_payment
            profile.is_subscribed = True
            profile.save()
            return HttpResponse(
                content=f'Webhook received: {event["type"]}.\
                    UserProfile payment data updated', status=200)

        except UserProfile.DoesNotExist:
            return HttpResponse(
                content=f'Webhook received: {event["type"]}.\
                    UserProfile does not exist.', status=404)
