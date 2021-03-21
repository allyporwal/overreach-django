from django.shortcuts import render


def active_workout(request):
    """Add workout to be stored in session, to be retrieved later
    on and saved in a Django JSONField"""
    workout = request.session.get('workout', {})
    workout_cleaned = None

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

        exercises = [{'exercise': a,
                      'sets': b,
                      'reps': c,
                      'set_volumes': []
                      } for (a, b, c) in zip(*exercises_sets_reps)]

        weights_lifted = [{'weight': a,
                           'rep_count': b,
                           'rpe': c
                           } for (a, b, c) in zip(*weight_rep_count_rpe)]

        for x, y in zip(exercises, set_count):
            z = int(y)
            sets_to_add = weights_lifted[0:z]
            x['set_volumes'].extend(sets_to_add)
            del weights_lifted[0:z]

    request.session['workout'] = workout_cleaned
    template = 'active_workout/active_workout.html'
    return render(request, template)
