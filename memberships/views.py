from django.shortcuts import render, get_object_or_404, redirect, reverse
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from django.conf import settings

import stripe
import json


def membership_signup(request):
    """Gather information from the user before payment"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
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
    user_email = profile.user.email

    template = 'memberships/checkout.html'
    context = {
        'profile': profile,
        'user_email': user_email,
        'stripe_public_key': stripe_public_key,
        # 'client_secret': intent.client_secret,
    }
    return render(request, template, context)
