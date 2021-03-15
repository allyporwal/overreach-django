from django.shortcuts import render
from .forms import WorkoutTrackerForm


# Create your views here.
def workout_tracker(request):

    if request.method == 'POST':

        form_data = {
            'session_name': request.POST['session_name'],
            'workout': request.POST['workout'],
        }

        form = WorkoutTrackerForm(form_data)

        if form.is_valid:
            form.save()

    form = WorkoutTrackerForm()
    template = 'workout_tracker/workout_tracker.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
