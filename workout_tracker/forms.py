from django import forms
from .models import WorkoutTracker, WorkoutComments


class WorkoutTrackerForm(forms.ModelForm):
    class Meta:
        model = WorkoutTracker
        fields = ('session_name',
                  'workout',
                  'session_reps',
                  'session_average_rpe',
                  'session_volume',
                  'session_notes',
                  )

    session_name = forms.CharField()
    workout = forms.JSONField(widget=forms.HiddenInput())
    session_reps = forms.IntegerField(widget=forms.HiddenInput())
    session_average_rpe = forms.FloatField(widget=forms.HiddenInput())
    session_volume = forms.FloatField(widget=forms.HiddenInput())
    session_notes = forms.Textarea()


class WorkoutCommentsForm(forms.ModelForm):
    class Meta:
        model = WorkoutComments
        exclude = ('comment_author',
                   'target_workout',
                   'comment_date')

    comment = forms.Textarea()
