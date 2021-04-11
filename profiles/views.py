from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile, Followers
from .forms import UserProfileForm


def profile(request, profile_id):
    """Show a user's profile page"""
    profile = get_object_or_404(UserProfile, pk=profile_id)
    number_of_workouts = len(profile.workouts.all())
    total_training_volume = sum(profile.workouts.values_list(
        'session_volume', flat=True))
    total_training_reps = sum(profile.workouts.values_list(
        'session_reps', flat=True))

    context = {
        'profile': profile,
        'number_of_workouts': number_of_workouts,
        'total_training_volume': total_training_volume,
        'total_training_reps': total_training_reps,
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


def add_follower(request, profile_id):
    """Allow a user to follow other users in a friends feed"""
    profile = get_object_or_404(UserProfile, pk=profile_id)
    follower = UserProfile.objects.get(user=request.user)

    follow = Followers.objects.create(
        follower=follower, is_following=profile,
        status=True
    )

    return redirect(reverse('dashboard'))
