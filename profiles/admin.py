from django.contrib import admin
from .models import Followers


class FollowersAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'follower',
        'is_following',
        'following_date',
    )

    ordering = ('pk',)


admin.site.register(Followers, FollowersAdmin)
