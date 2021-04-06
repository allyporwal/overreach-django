from django.contrib import admin
from .models import WorkoutTracker


class WorkoutTrackerAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'created_at',
        'created_by',
        'session_name',
    )

    ordering = ('pk',)


admin.site.register(WorkoutTracker, WorkoutTrackerAdmin)
