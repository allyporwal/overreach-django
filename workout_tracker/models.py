import uuid
from django.db import models


class WorkoutTracker(models.Model):
    workout_id = models.CharField(max_length=32, null=False, editable=False)
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
