from django.shortcuts import render


def active_workout(request):
    """Add workout to be stored in session, to be retrieved later
    on and saved in a Django JSONField"""
    workout = request.session.get('workout', {})

        

    template = 'active_workout/active_workout.html'
    return render(request, template)
