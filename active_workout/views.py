from django.shortcuts import render, redirect
from .validators import validate_active_workout


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
                    'set_volumes': []
                    } for (
                        exercise, sets, reps) in zip(*exercises_sets_reps)]

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
        for exercise, sets in zip(workout, set_count):
            sets_number = int(sets)
            sets_to_add = weights_lifted[0:sets_number]
            exercise['set_volumes'].extend(sets_to_add)
            del weights_lifted[0:sets_number]

        validate_active_workout(workout)
        # return redirect()

    # store the workout list to the session to be retrieved later
    request.session['workout'] = workout
    template = 'active_workout/active_workout.html'
    return render(request, template)
