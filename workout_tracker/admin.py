from django.contrib import admin
from .models import WorkoutTracker, WorkoutComments


class WorkoutTrackerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'created_at',
        'created_by',
        'session_name',
    )

    ordering = ('pk',)


admin.site.register(WorkoutTracker, WorkoutTrackerAdmin)


class WorkoutCommentsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'comment_date',
        'comment_author',
        'target_workout',
        'comment',
    )

    ordering = ('pk',)


admin.site.register(WorkoutComments, WorkoutCommentsAdmin)
