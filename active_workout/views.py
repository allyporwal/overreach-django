from django.shortcuts import render


def active_workout(request):
    """Add workout to be stored in session, to be retrieved later
    on and saved in a Django JSONField"""
    workout = request.session.get('workout', {})
    workout_cleaned = None

    # if request.method == 'POST':
    #     workout = request.POST.dict()
    #     workout_cleaned = {
    #         key: val for key, val in workout.items() if key !=
    #         'csrfmiddlewaretoken'}

    if request.method == 'POST':
        form_input_nested = [[], [], []]
        # grab values from all exercise, reps and set_type form fields
        for key, val in request.POST.items():
            if key.startswith('weight'):
                form_input_nested[0].append(val)
            if key.startswith('reps'):
                form_input_nested[1].append(val)
            if key.startswith('rpe'):
                form_input_nested[2].append(val)
            
        print(form_input_nested)
    # print(request.POST.keys())
    request.session['workout'] = workout_cleaned
    # print(request.session['workout'])
    template = 'active_workout/active_workout.html'
    return render(request, template)
