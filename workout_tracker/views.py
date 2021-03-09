from django.shortcuts import render
from .forms import WorkoutTrackerForm


# Create your views here.
def track_workout(request):

    if request.method == 'POST':
        form_data = {
            'session_name': request.POST['session_name'],
            'workout': request.POST['workout'],
        }
        form = WorkoutTrackerForm(form_data)
        if form.is_valid:
            form.save()

    form = WorkoutTrackerForm()
    template = 'workout_tracker/track_workout.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
