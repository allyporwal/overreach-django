from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile


# Create your views here.
def dashboard(request):
    '''Render the user's dashboard'''
    profile = get_object_or_404(UserProfile, user=request.user)
    recent_workouts = profile.workouts.all().order_by('-id')[:4]

    context = {
        'profile': profile,
        'recent_workouts': recent_workouts,
    }

    template = 'dashboard/dashboard.html'
    return render(request, template, context)
