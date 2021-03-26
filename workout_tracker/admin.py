from django.contrib import admin
from .models import WorkoutTracker


class WorkoutTrackerAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'created_by',
        'session_name',
        'workout',
        'pk',
    )

    ordering = ('pk',)


admin.site.register(WorkoutTracker, WorkoutTrackerAdmin)
