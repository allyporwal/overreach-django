from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import WorkoutTrackerForm
from profiles.models import UserProfile
from .models import WorkoutTracker
from active_workout.validators import validate_active_workout


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


def workout(request, workout_id):
    """Show an individual workout"""
    workout = get_object_or_404(WorkoutTracker, pk=workout_id)

    context = {
        'workout': workout,
    }

    return render(request, 'workout_tracker/workout.html', context)


def edit_workout(request, workout_id):
    """Allow a user to edit a workout they logged"""
    workout = get_object_or_404(WorkoutTracker, pk=workout_id)
    request.session['workout_to_edit'] = workout.workout

    context = {
        'workout': workout,
        'workout_to_edit': workout.workout,
    }

    return render(request, 'active_workout/edit_workout.html', context)


def delete_workout(request, workout_id):
    """Allow the user to delete a workout they logged"""
    workout = get_object_or_404(WorkoutTracker, pk=workout_id)
    if UserProfile.objects.get(user=request.user) == workout.created_by:
        workout.delete()
        return redirect(reverse('dashboard'))
    else:
        return redirect(reverse('active_workout'))


def all_workouts(request):
    """Display workouts done by everyone"""
    workouts = WorkoutTracker.objects.all()

    template = 'workout_tracker/all_workouts.html'
    context = {
        'workouts': workouts,
    }

    return render(request, template, context)
