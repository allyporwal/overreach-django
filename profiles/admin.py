from django.contrib import admin
from .models import Followers, UserProfile


class FollowersAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'follower',
        'is_following',
        'following_date',
    )

    ordering = ('pk',)


admin.site.register(Followers, FollowersAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'signup_date',
        'is_subscribed',
        'stripe_customer_id',
        'stripe_subscription_id',
        'default_billing_name',
        'default_billing_email',
    )

    ordering = ('signup_date',)


admin.site.register(UserProfile, UserProfileAdmin)
