from django import forms
from .models import WorkoutTracker


class WorkoutTrackerForm(forms.ModelForm):
    class Meta:
        model = WorkoutTracker
        fields = ('session_name', 'workout',)

    session_name = forms.CharField()
    workout = forms.JSONField()
