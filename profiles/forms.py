from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',
                   'is_subscribed',
                   'signup_date',
                   'stripe_customer_id',
                   'stripe_subscription_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'main_goals': 'What are your main training goals?',
            'image': 'Upload a profile picture',
            'default_billing_email': 'Email address associated with your card',
            'default_billing_name': 'Your name as it appears on your card',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County or State',
            'default_postcode': 'Postcode or Zipcode',
            'default_country': 'Country',
        }

        for field in self.fields:
            self.fields[field].label = labels[field]
