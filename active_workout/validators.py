from django.contrib import messages


def validate_active_workout(workout):
    """Perform validation on the workout input by the user
    before saving to to Django JSONField"""
    # Add all form values to arrays to be checked
    exercise_names = [exercise['exercise'] for exercise in workout]
    sets = [exercise['sets'] for exercise in workout]
    reps = [exercise['reps'] for exercise in workout]
    weights = []
    reps_lifted = []
    rate_perceived_exertion = []
    errors = []

    for exercise in workout:
        for weight in exercise['set_volumes']:
            weights.append(weight['weight'])
            reps_lifted.append(weight['rep_count'])
            rate_perceived_exertion.append(weight['rpe'])

    

    return errors
