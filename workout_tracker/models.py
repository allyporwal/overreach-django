from django.db import models
from profiles.models import UserProfile


class WorkoutTracker(models.Model):
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                   null=True, blank=True,
                                   related_name='workouts')
    created_at = models.DateTimeField(auto_now_add=True)
    session_name = models.CharField(max_length=50, null=False)
    workout = models.JSONField(blank=True)

    def __str__(self):
        return self.session_name
