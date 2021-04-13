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
        try:
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

        # render page with is_following as false to allow conditional
        # formatting in template
        except Followers.DoesNotExist:
            is_following = False
            context = {
                'displayed_profile': displayed_profile,
                'number_of_workouts': number_of_workouts,
                'total_training_volume': total_training_volume,
                'total_training_reps': total_training_reps,
                'is_following': is_following,
            }
        template = 'profiles/profile.html'
        return render(request, template, context)

    # displays the logged in user's own profile
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

    # prevent duplicate entries into Followers table
    try:
        is_follower_following = follower.follower.get(is_following=profile)
        # allow user to re-follow someone they previously unfollowed
        is_follower_following.status = True
        is_follower_following.save()
        return redirect(reverse('profile', args=[profile.id]))

    # only create entry if follower is not following the profile
    # of the user they're viewing
    except Followers.DoesNotExist:
        follow = Followers.objects.create(
            follower=follower, is_following=profile,
        )
        return redirect(reverse('profile', args=[profile.id]))


def unfollow(request, profile_id):
    """Allow a user to unfollow another user"""
    profile = get_object_or_404(UserProfile, pk=profile_id)
    follower = UserProfile.objects.get(user=request.user)

    # modify the status field in the database entry
    try:
        is_following = follower.follower.get(is_following=profile)
        is_following.status = False
        is_following.save()
        return redirect(reverse('profile', args=[profile.id]))

    # redirect if user uses url but doesn't follow profile
    except Followers.DoesNotExist:
        return redirect(reverse('dashboard'))


def friends(request):
    """A feed showing more detailed overview of friends' workouts,
    more data on display in the template than the all_workouts view"""
    profile = get_object_or_404(UserProfile, user=request.user)
    # filter out people the user has unfollowed
    friends = profile.follower.values('is_following').filter(status=True)
    friends_profiles = UserProfile.objects.filter(pk__in=friends)
    friends_workouts = WorkoutTracker.objects.filter(
        created_by__in=friends_profiles)

    template = 'profiles/friends.html'
    context = {
        'profile': profile,
        'friends_profiles': friends_profiles,
        'friends_workouts': friends_workouts,
    }
    return render(request, template, context)
