from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """Show the user's profile page, allowing them to edit their details"""
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {

    }
    template = 'profiles/profile.html'
    return render(request, template, context)


def edit_profile(request):
    """Allow the user to edit their profile details"""
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'image': request.POST['image'],
            'default_street_address1': request.POST['default_street_address1'],
            'default_street_address2': request.POST['default_street_address2'],
            'default_town_or_city': request.POST['default_town_or_city'],
            'default_county': request.POST['default_county'],
            'default_postcode': request.POST['default_postcode'],
            'default_country': request.POST['default_country'],
        }

        form = UserProfileForm(form_data, instance=profile)

        if form.is_valid:
            form.save()

    form = UserProfileForm(instance=profile)
    context = {
        'form': form,
    }
    template = 'profiles/edit_profile.html'
    return render(request, template, context)
