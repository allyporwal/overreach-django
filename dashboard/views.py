import json
import datetime
from django.shortcuts import render, get_object_or_404
from profiles.models import UserProfile


# Create your views here.
def dashboard(request):
    '''Render the user's dashboard'''
    profile = get_object_or_404(UserProfile, user=request.user)
    recent_workouts = profile.workouts.all().order_by('-id')[:4]
    chart_data_raw = profile.workouts.values('session_average_rpe')[:8]
    created_at = profile.workouts.values_list('created_at', flat=True)[:8]

    chart_data = json.dumps(list(chart_data_raw))
    only_date_raw = list(created_at)
    only_date = []

    for date in only_date_raw:
        date.strftime('%d/%m/%Y')
        only_date.append(date.strftime('%d/%m/%Y'))

    context = {
        'profile': profile,
        'recent_workouts': recent_workouts,
        'chart_data': chart_data,
        'created_at': created_at,
        'only_date': only_date,
    }

    template = 'dashboard/dashboard.html'
    return render(request, template, context)
