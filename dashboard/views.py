from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile


# Create your views here.
def dashboard(request):
    '''Render the user's dashboard'''
    profile = get_object_or_404(UserProfile, user=request.user)
    workouts = profile.workouts.all()

    context = {
        'profile': profile,
        'workouts': workouts,
    }

    template = 'dashboard/dashboard.html'
    return render(request, template, context)
