def workout_in_progress(request):

    workout = request.session.get('workout', {})
    workout_edited = request.session.get('workout_edited', {})
    in_progress = True if workout != {} else False
    edit_in_progress = True if workout_edited != {} else False

    context = {
        'workout': workout,
        'workout_edited': workout_edited,
        'in_progress': in_progress,
        'edit_in_progress': edit_in_progress,
    }

    return context
