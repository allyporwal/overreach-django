import json
import stripe
from django.shortcuts import render, get_object_or_404, redirect, reverse
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def membership_signup(request):
    """Gather information from the user before payment"""
    profile = get_object_or_404(UserProfile, user=request.user)
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        form = UserProfileForm(request.post, request.files)
        stripe.api_key = stripe_secret_key
        # form_data = {
        #     'first_name': request.POST['first_name'],
        #     'last_name': request.POST['last_name'],
        #     'main_goals': request.POST['main_goals'],
        #     'image': request.POST['image'],
        #     'default_billing_email': request.POST['default_billing_email'],
        #     'default_billing_name': request.POST['default_billing_name'],
        #     'default_street_address1': request.POST['default_street_address1'],
        #     'default_street_address2': request.POST['default_street_address2'],
        #     'default_town_or_city': request.POST['default_town_or_city'],
        #     'default_county': request.POST['default_county'],
        #     'default_postcode': request.POST['default_postcode'],
        #     'default_country': request.POST['default_country'],
        # }
        # form = UserProfileForm(form_data, instance=profile)

        if form.is_valid():
            # create a customer object in Stripe using form data
            subscriber = stripe.Customer.create(
                email=request.POST['default_billing_email'],
                name=request.POST['default_billing_name'],
                address={
                    'line1': request.POST['default_street_address1'],
                    'line2': request.POST['default_street_address2'],
                    'city': request.POST['default_town_or_city'],
                    'state': request.POST['default_county'],
                    'postal_code': request.POST['default_postcode'],
                    'country': request.POST['default_country'],
                })
            # assign the Stripe customer ID to
            # the user's linked userprofile
            profile.stripe_customer_id = subscriber.id
            form.save()
            return redirect(reverse('checkout'))
        else:
            messages.error(request, 'Please ensure the form is valid.')

    else:
        form = UserProfileForm()

    # form = UserProfileForm(instance=profile)
    template = 'memberships/membership_signup.html'
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template, context)


@login_required
def checkout(request):
    """The payment view"""
    profile = get_object_or_404(UserProfile, user=request.user)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    # pass data needed to set up subscription
    price_id = settings.STRIPE_PRICE_ID
    customer_id = profile.stripe_customer_id
    billing_name = profile.default_billing_name
    billing_email = profile.default_billing_email

    template = 'memberships/checkout.html'
    context = {
        'profile': profile,
        'stripe_public_key': stripe_public_key,
        'price_id': price_id,
        'customer_id': customer_id,
        'billing_name': billing_name,
        'billing_email': billing_email,
    }
    return render(request, template, context)


@login_required
def checkout_success(request):
    """If successful checkout, user sees this page"""
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'memberships/checkout_success.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


@login_required
def membership_status(request):
    """Show the user their membership status and give
    option to cancel"""
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'memberships/membership_status.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


@login_required
def cancel_membership(request):
    """Allow user to cancel their membership"""
    profile = get_object_or_404(UserProfile, user=request.user)
    subscription_id = profile.stripe_subscription_id

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        stripe.Subscription.delete(subscription_id)
        profile.is_subscribed = False
    except Exception as e:
        return JsonResponse({'error': (e.args[0])}, status=403)

    return redirect(reverse('membership_cancelled'))


@login_required
def membership_cancelled(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'memberships/membership_cancelled.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


@login_required
@require_POST
def create_subscription(request):
    """Create the subscription, adapted from
    Stripe documentation, link in readme"""
    stripe.api_key = settings.STRIPE_SECRET_KEY
    data = json.loads(request.body.decode('utf-8'))

    try:
        # Attach the payment method to the customer
        stripe.PaymentMethod.attach(
            data['paymentMethodId'],
            customer=data['customerId'],
        )
        # Set the default payment method on the customer
        stripe.Customer.modify(
            data['customerId'],
            invoice_settings={
                'default_payment_method': data['paymentMethodId'],
            },
        )
        # Create the subscription
        subscription = stripe.Subscription.create(
            customer=data['customerId'],
            items=[
                {
                    'price': settings.STRIPE_PRICE_ID
                }
            ],
            expand=['latest_invoice.payment_intent'],
        )

        return JsonResponse(subscription)
    except Exception as e:
        return JsonResponse({'error': (e.args[0])}, status=403)
