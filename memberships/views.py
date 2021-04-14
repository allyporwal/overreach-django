from django.shortcuts import render, get_object_or_404, redirect, reverse
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from django.conf import settings

import stripe
import json


def membership_signup(request):
    """Gather information from the user before payment"""
    profile = get_object_or_404(UserProfile, user=request.user)
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        stripe.api_key = stripe_secret_key
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'main_goals': request.POST['main_goals'],
            'image': request.POST['image'],
            'default_billing_email': request.POST['default_billing_email'],
            'default_billing_name': request.POST['default_billing_name'],
            'default_street_address1': request.POST['default_street_address1'],
            'default_street_address2': request.POST['default_street_address2'],
            'default_town_or_city': request.POST['default_town_or_city'],
            'default_county': request.POST['default_county'],
            'default_postcode': request.POST['default_postcode'],
            'default_country': request.POST['default_country'],
        }
        form = UserProfileForm(form_data, instance=profile)

        if form.is_valid():
            subscriber = stripe.Customer.create(
                email=request.POST['default_billing_email'],
                name=request.POST['default_billing_name'])
            profile.stripe_customer_id = subscriber.id
            form.save()
            return redirect(reverse('checkout'))

    form = UserProfileForm(instance=profile)
    template = 'memberships/membership_signup.html'
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template, context)


def checkout(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    price_id = settings.STRIPE_PRICE_ID
    customer_id = profile.stripe_customer_id
    billing_name = profile.default_billing_name
    billing_email = profile.default_billing_email

    template = 'memberships/checkout.html'
    context = {
        'profile': profile,
        'stripe_public_key': stripe_public_key,
        'price_id': price_id,
        'customer_id': customer_id,
        'billing_name': billing_name,
        'billing_email': billing_email,
        # 'client_secret': intent.client_secret,
    }
    return render(request, template, context)
