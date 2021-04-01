from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """Show the user's profile page, allowing them to edit their details"""
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {

    }
    template = 'profiles/profile.html'
    return render(request, template, context)


def edit_profile(request):
    """Allow the user to edit their profile details"""
    form = UserProfileForm()

    context = {
        'form': form,
    }
    template = 'profiles/edit_profile.html'
    return render(request, template, context)
