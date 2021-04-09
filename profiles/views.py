from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request, profile_id):
    """Show the user's profile page"""
    profile = get_object_or_404(UserProfile, pk=profile_id)
    number_of_workouts = len(profile.workouts.all())

    context = {
        'profile': profile,
        'number_of_workouts': number_of_workouts,
    }
    template = 'profiles/profile.html'
    return render(request, template, context)


def edit_profile(request):
    """Allow the user to edit their profile details"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, template, context)
