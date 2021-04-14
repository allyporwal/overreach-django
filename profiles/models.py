from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """User profile to hold billing information,
    profile image and workout history"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signup_date = models.DateTimeField(auto_now_add=True)
    is_subscribed = models.BooleanField(default=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    main_goals = models.TextField(max_length=350, blank=True, null=False)
    image = models.ImageField(null=True, blank=True)
    default_billing_name = models.CharField(max_length=64)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=40,
                                      null=True, blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True),
    stripe_customer_id = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Followers(models.Model):
    """Model that allows users to follow other users on their friends feed"""
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                 null=False, blank=False,
                                 related_name='follower')
    is_following = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     null=False, blank=False,
                                     related_name='is_following')
    following_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.is_following.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
