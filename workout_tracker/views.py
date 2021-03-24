from django.shortcuts import render, redirect, reverse
from .forms import WorkoutTrackerForm


# Create your views here.
def log_workout(request):

    if request.method == 'POST':

        form_data = {
            'session_name': request.POST['session_name'],
            'workout': request.session['workout'],
        }

        form = WorkoutTrackerForm(form_data)

        if form.is_valid:
            form.save()
            del request.session['workout']
            return redirect(reverse('home'))

    form = WorkoutTrackerForm()
    template = 'workout_tracker/log_workout.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
