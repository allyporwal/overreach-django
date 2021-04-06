from django import forms
from .models import WorkoutTracker


class WorkoutTrackerForm(forms.ModelForm):
    class Meta:
        model = WorkoutTracker
        fields = ('session_name',
                  'workout',
                  'session_reps',
                  'session_average_rpe',
                  'session_volume',
                  )

    session_name = forms.CharField()
    workout = forms.JSONField(widget=forms.HiddenInput())
    session_reps = forms.IntegerField(widget=forms.HiddenInput())
    session_average_rpe = forms.FloatField(widget=forms.HiddenInput())
    session_volume = forms.FloatField(widget=forms.HiddenInput())
