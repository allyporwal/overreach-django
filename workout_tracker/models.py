from django.db import models
from profiles.models import UserProfile


class WorkoutTracker(models.Model):
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                   null=True, blank=True,
                                   related_name='workouts')
    created_at = models.DateTimeField(auto_now_add=True)
    session_name = models.CharField(max_length=50, null=False)
    workout = models.JSONField(blank=False, null=False)
    session_reps = models.IntegerField(blank=False, null=False)
    session_average_rpe = models.FloatField(blank=False, null=False)
    session_volume = models.FloatField(blank=False, null=False)
    session_notes = models.TextField(max_length=350, blank=True, null=False)

    def __str__(self):
        return self.session_name


class WorkoutComments(models.Model):
    comment_author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                       null=False, blank=False,
                                       related_name='comment_author')
    target_workout = models.ForeignKey(WorkoutTracker,
                                       on_delete=models.CASCADE,
                                       null=False, blank=False,
                                       related_name='target_workout')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.comment_author.user.username


