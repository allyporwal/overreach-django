from django.conf import settings


def workout_in_progress(request):

    workout = request.session.get('workout', {})
    in_progress = True if workout != {} else False

    context = {
        'workout': workout,
        'in_progress': in_progress,
    }

    return context
