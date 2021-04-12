from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile, Followers
from .forms import UserProfileForm
from workout_tracker.models import WorkoutTracker


def profile(request, profile_id):
    """Show a user's profile page"""
    profile = get_object_or_404(UserProfile, user=request.user)
    displayed_profile = get_object_or_404(UserProfile, pk=profile_id)

    # display some all time statistics from the profile's workouts
    number_of_workouts = len(displayed_profile.workouts.all())
    total_training_volume = sum(displayed_profile.workouts.values_list(
        'session_volume', flat=True))
    total_training_reps = sum(displayed_profile.workouts.values_list(
        'session_reps', flat=True))

    # On another profile page check to see if user is following displayed user
    if profile != displayed_profile:
        is_following = profile.follower.get(is_following=displayed_profile)

        context = {
            'displayed_profile': displayed_profile,
            'number_of_workouts': number_of_workouts,
            'total_training_volume': total_training_volume,
            'total_training_reps': total_training_reps,
            'is_following': is_following,
        }
        template = 'profiles/profile.html'
        return render(request, template, context)

    # return the user's public profile page otherwise
    context = {
            'displayed_profile': displayed_profile,
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
    )

    return redirect(reverse('dashboard'))


def unfollow(request, profile_id):
    """Allow a user to unfollow another user"""



def friends(request):
    """A feed showing more detailed overview of friends' workouts,
    more data on display in the template than the all_workouts view"""
    profile = get_object_or_404(UserProfile, user=request.user)
    friends = profile.follower.values('is_following')
    friends_profiles = UserProfile.objects.filter(pk__in=friends)
    friends_workouts = WorkoutTracker.objects.filter(
        created_by__in=friends_profiles)
    
    print(len(friends_profiles))

    friend_status = profile.follower.values('status')
    print(friend_status)

    template = 'profiles/friends.html'
    context = {
        'profile': profile,
        'friends': friends,
        'friends_workouts': friends_workouts,
    }
    return render(request, template, context)