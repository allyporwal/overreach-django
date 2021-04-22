from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from .forms import WorkoutTrackerForm, WorkoutCommentsForm
from profiles.models import UserProfile
from .models import WorkoutTracker, WorkoutComments, WorkoutLikes
from .validators import validate_active_workout
from django.contrib.auth.decorators import login_required


@login_required
def active_workout(request):
    """Add workout to be stored in session, to be retrieved later
    on and saved in a Django JSONField"""
    workout = request.session.get('workout', {})

    # Take all form information from post and sort into nested lists
    # by using endswith and startswith methods on the form keys
    if request.method == 'POST':
        exercises_sets_reps = [[], [], []]
        set_count = exercises_sets_reps[1]
        weight_rep_count_rpe = [[], [], []]
        # check_for_empty = exercises_sets_reps + weight_rep_count_rpe
        for key, val in request.POST.items():
            if key.endswith('-name'):
                exercises_sets_reps[0].append(val)
            if key.endswith('-sets'):
                exercises_sets_reps[1].append(val)
            if key.endswith('-reps'):
                exercises_sets_reps[2].append(val)
            if key.startswith('weight'):
                weight_rep_count_rpe[0].append(val)
            if key.startswith('reps'):
                weight_rep_count_rpe[1].append(val)
            if key.startswith('rpe'):
                weight_rep_count_rpe[2].append(val)

        # Create lists of objects from above arrays using list comprehension
        # Attribution for this snippet in README
        workout = [{'exercise': exercise,
                    'sets': sets,
                    'reps': reps,
                    'set_volumes': [],
                    } for (
                        exercise, sets, reps) in zip(*exercises_sets_reps)]

        weights_lifted = [{'weight': weight,
                           'rep_count': rep_count,
                           'rpe': rpe,
                           } for (
                               weight, rep_count, rpe) in zip(
                                   *weight_rep_count_rpe)]

        # Iterate through workout and set_count lists,
        # add the correct number of sets to each dictionary
        # in the workout list and then delete them from the
        # weights_lifted list
        for exercise, sets in zip(workout, set_count):
            sets_number = int(sets)
            sets_to_add = weights_lifted[0:sets_number]
            exercise['set_volumes'].extend(sets_to_add)
            del weights_lifted[0:sets_number]

        # store the workout list to the session to be retrieved later
        request.session['workout'] = workout

        # validate the workout data
        errors = validate_active_workout(request.session['workout'])

        # redirect back to the form if validation fails, showing user a
        # list of any errors that must be corrected before workout can
        # be saved
        if errors != []:
            context = {
                'errors': errors,
            }
            template = 'workout_tracker/active_workout.html'
            return render(request, template, context)

        else:
            return redirect(reverse('log_workout'))

    template = 'workout_tracker/active_workout.html'
    return render(request, template)


@login_required
def delete_active_workout(request):
    """Delete the active workout from the session"""
    workout = request.session.get('workout', {})

    if workout:
        del request.session['workout']
        return redirect(reverse('dashboard'))

    else:
        return redirect(reverse('dashboard'))


@login_required
def log_workout(request):
    """Stores a user's workout to the database"""
    workout_to_log = request.session['workout']

    # sort workout data into lists for processing
    set_count = []
    reps_lifted = []
    rate_perceived_exertion = []
    session_rpe = []
    volumes = []

    for exercise in workout_to_log:
        set_count.append(int(exercise['sets']))
        for weight in exercise['set_volumes']:
            reps_lifted.append(int(weight['rep_count']))
            rate_perceived_exertion.append(float(weight['rpe']))
            session_rpe.append(float(weight['rpe']))
            volumes.append(
                (float(weight['rep_count']) * float(weight['weight'])))

    # data for each individual exercise to calculate overall workout metrics
    exercise_volumes = []
    exercise_reps = []

    for sets in set_count:
        exercise_volumes.append(sum(volumes[0:sets]))
        exercise_reps.append(sum(reps_lifted[0:sets]))
        del volumes[0:sets]
        del reps_lifted[0:sets]
        del rate_perceived_exertion[0:sets]

    # workout metrics to be saved in database
    session_reps = sum(exercise_reps)
    session_average_rpe = round(sum(session_rpe) / len(session_rpe), 2)
    session_volume = sum(exercise_volumes)

    if request.method == 'POST':

        # Allow the user to name their workout and
        # grab the workout from the session to store
        # in Django JSONField
        form_data = {
            'session_name': request.POST['session_name'],
            'workout': request.session['workout'],
            'session_reps': session_reps,
            'session_average_rpe': session_average_rpe,
            'session_volume': session_volume,
            'session_notes': request.POST['session_notes']
        }

        form = WorkoutTrackerForm(form_data)

        if form.is_valid:
            workout = form.save(commit=False)
            # attach the workout to the user's profile
            workout.created_by = UserProfile.objects.get(user=request.user)
            workout.save()
            # clear the workout from the session after saving
            del request.session['workout']
            return redirect(reverse('workout', args=[workout.id]))

    form = WorkoutTrackerForm()

    template = 'workout_tracker/log_workout.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def workout(request, workout_id):
    """Show an individual workout"""
    workout = get_object_or_404(WorkoutTracker, pk=workout_id)
    comments = workout.target_workout.all()
    likes = workout.liked_workout.filter(like_status=True)

    # sort workout data into lists for processing
    set_count = []
    reps_lifted = []
    rate_perceived_exertion = []
    session_rpe = []
    volumes = []

    for exercise in workout.workout:
        set_count.append(int(exercise['sets']))
        for weight in exercise['set_volumes']:
            reps_lifted.append(int(weight['rep_count']))
            rate_perceived_exertion.append(float(weight['rpe']))
            session_rpe.append(float(weight['rpe']))
            volumes.append(
                (float(weight['rep_count']) * float(weight['weight'])))

    # data for each individual exercise
    exercise_volumes = []
    exercise_reps = []
    exercise_average_rpe = []

    for sets in set_count:
        exercise_volumes.append(sum(volumes[0:sets]))
        exercise_reps.append(sum(reps_lifted[0:sets]))
        exercise_average_rpe.append(round(sum(
            rate_perceived_exertion[0:sets]) / sets, 2))
        del volumes[0:sets]
        del reps_lifted[0:sets]
        del rate_perceived_exertion[0:sets]

    # data zipped for easier access in template
    workout_zipped = zip(
        workout.workout, exercise_volumes, exercise_reps, exercise_average_rpe)

    form = WorkoutCommentsForm()
    template = 'workout_tracker/workout.html'
    context = {
        'workout': workout,
        'workout_zipped': workout_zipped,
        'form': form,
        'comments': comments,
        'likes': likes,
    }
    return render(request, template, context)


@login_required
def edit_workout(request, workout_id):
    """Allow a user to edit a workout they logged"""
    workout = get_object_or_404(WorkoutTracker, pk=workout_id)
    request.session['workout_to_edit'] = workout.workout

    # Check that the user created the workout they want to edit
    if UserProfile.objects.get(user=request.user) == workout.created_by:

        # Take all form information from post and sort into nested lists
        # by using endswith and startswith methods on the form keys
        if request.method == 'POST':
            exercises_sets_reps = [[], [], []]
            set_count = exercises_sets_reps[1]
            weight_rep_count_rpe = [[], [], []]
            for key, val in request.POST.items():
                if key.endswith('-name'):
                    exercises_sets_reps[0].append(val)
                if key.endswith('-sets'):
                    exercises_sets_reps[1].append(val)
                if key.endswith('-reps'):
                    exercises_sets_reps[2].append(val)
                if key.startswith('weight'):
                    weight_rep_count_rpe[0].append(val)
                if key.startswith('reps'):
                    weight_rep_count_rpe[1].append(val)
                if key.startswith('rpe'):
                    weight_rep_count_rpe[2].append(val)

            # Create lists of objects from above arrays
            # Attribution for this snippet in README
            workout_edited = [{'exercise': exercise,
                               'sets': sets,
                               'reps': reps,
                               'set_volumes': []
                               } for (
                                   exercise, sets, reps) in zip(
                                       *exercises_sets_reps)]

            weights_lifted = [{'weight': weight,
                               'rep_count': rep_count,
                               'rpe': rpe
                               } for (
                                   weight, rep_count, rpe) in zip(
                                       *weight_rep_count_rpe)]

            # Iterate through workout and set_count lists,
            # add the correct number of sets to each dictionary
            # in the workout list and then delete them from the
            # weights_lifted list
            for exercise, sets in zip(workout_edited, set_count):
                sets_number = int(sets)
                sets_to_add = weights_lifted[0:sets_number]
                exercise['set_volumes'].extend(sets_to_add)
                del weights_lifted[0:sets_number]

            # clear workout to edit from session to replace with edited workout
            # del request.session['workout_to_edit']
            # store the workout list to the session to be retrieved later
            request.session['workout_edited'] = workout_edited

            # validate the workout data
            errors = validate_active_workout(request.session['workout_edited'])

            # redirect back to the form if validation fails, showing user a
            # list of any errors that must be corrected before workout can
            # be saved
            if errors != []:
                context = {
                    'workout': workout,
                    'errors': errors,
                }
                template = 'workout_tracker/edit_workout.html'
                return render(request, template, context)

            else:
                return redirect(reverse('update_workout', args=[workout.id]))
    else:
        return redirect(reverse('dashboard'))

    template = 'workout_tracker/edit_workout.html'
    context = {
        'workout': workout,
        'workout_to_edit': workout.workout,
    }
    return render(request, template, context)


@login_required
def update_workout(request, workout_id):
    """Updates a user's workout in the database"""
    workout_to_update = get_object_or_404(WorkoutTracker, pk=workout_id)
    workout_edited = request.session.get('workout_edited', {})
    edit_in_progress = True if workout_edited != {} else False

    if edit_in_progress:
        # sort workout data into lists for processing
        set_count = []
        reps_lifted = []
        rate_perceived_exertion = []
        session_rpe = []
        volumes = []

        for exercise in workout_edited:
            set_count.append(int(exercise['sets']))
            for weight in exercise['set_volumes']:
                reps_lifted.append(int(weight['rep_count']))
                rate_perceived_exertion.append(float(weight['rpe']))
                session_rpe.append(float(weight['rpe']))
                volumes.append(
                    (float(weight['rep_count']) * float(weight['weight'])))

        # data for each individual exercise
        # to calculate overall workout metrics
        exercise_volumes = []
        exercise_reps = []

        for sets in set_count:
            exercise_volumes.append(sum(volumes[0:sets]))
            exercise_reps.append(sum(reps_lifted[0:sets]))
            del volumes[0:sets]
            del reps_lifted[0:sets]
            del rate_perceived_exertion[0:sets]

        # workout metrics to be saved in database
        session_reps = sum(exercise_reps)
        session_average_rpe = round(sum(session_rpe) / len(session_rpe), 2)
        session_volume = sum(exercise_volumes)

        # Check that the user created the workout they want to edit
        if UserProfile.objects.get(
                user=request.user) == workout_to_update.created_by:

            if request.method == 'POST':

                # Allow the user to re-name their workout and
                # grab the workout from the session to store
                # in Django JSONField
                form_data = {
                    'session_name': request.POST['session_name'],
                    'workout': workout_edited,
                    'session_reps': session_reps,
                    'session_average_rpe': session_average_rpe,
                    'session_volume': session_volume,
                    'session_notes': request.POST['session_notes']
                }

                form = WorkoutTrackerForm(
                    form_data, instance=workout_to_update)

                if form.is_valid:
                    form.save()
                    # clear the workout from the session after saving
                    del request.session['workout_to_edit']
                    del request.session['workout_edited']
                    return redirect(reverse(
                        'workout', args=[workout_to_update.id]))

        else:
            return redirect(reverse('dashboard'))

    else:
        return redirect(reverse('dashboard'))

    form = WorkoutTrackerForm(initial={
            'session_name': workout_to_update.session_name,
            'session_notes': workout_to_update.session_notes,
        })

    template = 'workout_tracker/update_workout.html'
    context = {
        'workout': workout_to_update,
        'form': form,
    }
    return render(request, template, context)


@login_required
def delete_workout(request, workout_id):
    """Allow the user to delete a workout they logged"""
    workout = get_object_or_404(WorkoutTracker, pk=workout_id)

    if UserProfile.objects.get(user=request.user) == workout.created_by:
        workout.delete()
        return redirect(reverse('dashboard'))
    else:
        return redirect(reverse('dashboard'))


@login_required
def all_workouts(request):
    """Display workouts done by everyone"""
    workouts = WorkoutTracker.objects.all().order_by('-pk')
    workout_paginator = Paginator(workouts, 12)

    page_number = request.GET.get('page')
    page_obj = workout_paginator.get_page(page_number)

    template = 'workout_tracker/all_workouts.html'
    context = {
        'workouts': workouts,
        'page_obj': page_obj,
    }
    return render(request, template, context)


@login_required
def comment_on_workout(request, workout_id):
    """Allow a user to comment on a workout"""
    profile = UserProfile.objects.get(user=request.user)
    workout = get_object_or_404(WorkoutTracker, pk=workout_id)

    if request.method == 'POST':

        form_data = {
            'comment': request.POST['comment'],
        }

        form = WorkoutCommentsForm(form_data)

        if form.is_valid:
            comment = form.save(commit=False)
            comment.target_workout = workout
            comment.comment_author = profile
            comment.save()

            return redirect(reverse('workout', args=[workout.id]))


@login_required
def like_workout(request, workout_id):
    """Allow a user to like another user's workout"""
    profile = UserProfile.objects.get(user=request.user)
    workout = WorkoutTracker.objects.get(pk=workout_id)

    # prevent duplicate entries into WorkoutLikes table
    try:
        has_user_liked = workout.liked_workout.get(liker=profile)
        # allow user to re-follow someone they previously unfollowed
        has_user_liked.like_status = True
        has_user_liked.save()

        return redirect(reverse('workout', args=[workout.id]))

    # only create entry if follower is not following the profile
    # of the user they're viewing
    except WorkoutLikes.DoesNotExist:
        like = WorkoutLikes.objects.create(
            liked_workout=workout, liker=profile,
        )
        return redirect(reverse('workout', args=[workout.id]))
