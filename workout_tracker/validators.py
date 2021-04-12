def validate_active_workout(workout):
    """Perform validation on the workout input by the user
    before saving to to Django JSONField"""
    # Add all workout values to arrays to be checked
    exercise_names = [exercise['exercise'] for exercise in workout]
    sets = [int(exercise['sets']) for exercise in workout]
    reps = [int(exercise['reps']) for exercise in workout]
    weights = []
    reps_lifted = []
    rate_perceived_exertion = []
    #  function will return a list of errors to be used in views and templates
    errors = []

    for exercise in workout:
        for weight in exercise['set_volumes']:
            weights.append(float(weight['weight']))
            reps_lifted.append(int(weight['rep_count']))
            rate_perceived_exertion.append(float(weight['rpe']))

    if '' in exercise_names:
        errors.append("Please ensure you input a name for every exercise")

    for set_number in sets:
        if set_number <= 0:
            errors.append("You can't lift negative or zero sets!")
        elif set_number == '':
            errors.append("Please input how many sets you want to lift")

    for rep in reps:
        if rep < 0:
            errors.append("You can't lift negative reps!")
        if rep > 250:
            errors.append("You can't log more than 250 reps of one exercise \
                          in a single set")

    for weight in weights:
        if weight < 0:
            errors.append("You can't lift negative kilos!")
        if weight > 1200:
            errors.append("You can't lift more than 1200kg in a single rep")

    for reps_logged in reps_lifted:
        if reps_logged < 0:
            errors.append("You can't lift negative reps!")
        if reps_logged > 250:
            errors.append("You can't log more than 250 reps of one exercise \
                          in a single set")

    for rpe in rate_perceived_exertion:
        if rpe < 1:
            errors.append("RPE must be between 1 and 10")
        if rpe > 10:
            errors.append("RPE must be between 1 and 10")

    return errors
