import uuid
from django.db import models
from profiles.models import UserProfile


class WorkoutTracker(models.Model):
    workout_id = models.CharField(max_length=32, null=False, editable=False)
    created_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                   null=True, blank=True,
                                   related_name='workouts')
    created_at = models.DateTimeField(auto_now_add=True)
    session_name = models.CharField(max_length=50, null=False)
    workout = models.JSONField(blank=True)

    def _generate_workout_id(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.workout_id:
            self.workout_id = self._generate_workout_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.workout_id
