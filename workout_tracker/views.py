from django.shortcuts import render, redirect, reverse
from .forms import WorkoutTrackerForm
from profiles.models import UserProfile


# Create your views here.
def log_workout(request):

    if request.method == 'POST':

        form_data = {
            'session_name': request.POST['session_name'],
            'workout': request.session['workout'],
        }

        form = WorkoutTrackerForm(form_data)

        if form.is_valid:
            workout = form.save(commit=False)
            workout.created_by = UserProfile.objects.get(user=request.user)
            workout.save()
            del request.session['workout']
            return redirect(reverse('dashboard'))

    form = WorkoutTrackerForm()
    template = 'workout_tracker/log_workout.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
