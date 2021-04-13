from django.shortcuts import render, get_object_or_404, redirect, reverse
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from django.conf import settings


# Create your views here.
def membership_signup(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect(reverse('checkout'))

    form = UserProfileForm(instance=profile)
    template = 'memberships/membership_signup.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def checkout(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    template = 'memberships/checkout.html'
    context = {
        'profile': profile,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test',
    }
    return render(request, template, context)
