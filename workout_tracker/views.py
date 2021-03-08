from django.shortcuts import render
from .forms import WorkoutTrackerForm


# Create your views here.
def track_workout(request):
    if request.method == 'POST':
        form = WorkoutTrackerForm()

    form = WorkoutTrackerForm()
    template = 'workout_tracker/track_workout.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
