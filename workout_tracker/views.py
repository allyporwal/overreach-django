from django.shortcuts import render, redirect, reverse
from .forms import WorkoutTrackerForm
from profiles.models import UserProfile


def log_workout(request):
    """Stores a user's workout to the database"""
    if request.method == 'POST':

        # Allow the user to name their workout and
        # grab the workout from the session to store
        # in Django JSONField
        form_data = {
            'session_name': request.POST['session_name'],
            'workout': request.session['workout'],
        }

        form = WorkoutTrackerForm(form_data)

        if form.is_valid:
            workout = form.save(commit=False)
            # attach the workout to the user's profile
            workout.created_by = UserProfile.objects.get(user=request.user)
            workout.save()
            # clear the workout from the session after saving
            del request.session['workout']
            return redirect(reverse('dashboard'))

    form = WorkoutTrackerForm()
    template = 'workout_tracker/log_workout.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
