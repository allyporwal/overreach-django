from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile
from workout_tracker.models import WorkoutTracker
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def check_membership(user):
    profile = UserProfile.objects.get(user=user)
    if profile.is_subscribed:
        return profile


@login_required
@user_passes_test(check_membership, login_url='/memberships/signup/')
def dashboard(request):
    '''Render the user's dashboard'''
    profile = get_object_or_404(UserProfile, user=request.user)

    # load four most recent workouts to display
    recent_workouts = profile.workouts.all().order_by('-id')[:2]

    # retreive data from last 8 workouts to display on graphs
    average_rpe_raw = profile.workouts.values('session_average_rpe')[:8]
    session_volume_raw = profile.workouts.values('session_volume')[:8]
    session_reps_raw = profile.workouts.values('session_reps')[:8]
    created_at = profile.workouts.values_list('created_at', flat=True)[:8]

    # put workout data into flat lists
    average_rpe = [d['session_average_rpe'] for d in average_rpe_raw]
    session_volume = [d['session_volume'] for d in session_volume_raw]
    session_reps = [d['session_reps'] for d in session_reps_raw]

    # get datetime into useable format for graph labels
    only_date_raw = list(created_at)
    only_date = []

    for date in only_date_raw:
        only_date.append(date.strftime('%d/%m/%Y, %H:%M'))

    # zip all data into lists of dicts for graphing in JS on template
    rpe_chart_data = [{
        'x': date,
        'y': rpe,
    } for date, rpe in zip(only_date, average_rpe)]

    total_volume_chart_data = [{
        'x': date,
        'y': volume,
    } for date, volume in zip(only_date, session_volume)]

    total_reps_chart_data = [{
        'x': date,
        'y': reps,
    } for date, reps in zip(only_date, session_reps)]

    # load friends most recent 2 workouts
    friends = profile.follower.values('is_following').filter(status=True)
    friends_profiles = UserProfile.objects.filter(pk__in=friends)
    friends_workouts = WorkoutTracker.objects.filter(
        created_by__in=friends_profiles).order_by('-id')[:2]

    template = 'dashboard/dashboard.html'
    context = {
        'profile': profile,
        'recent_workouts': recent_workouts,
        'rpe_chart_data': rpe_chart_data,
        'total_volume_chart_data': total_volume_chart_data,
        'total_reps_chart_data': total_reps_chart_data,
        'friends_workouts': friends_workouts,
        'friends': friends,
    }
    return render(request, template, context)
