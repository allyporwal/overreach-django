// set up Stripe keys and style
let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();
let style = {
    base: {
      color: '#303238',
      fontSize: '16px',
      fontFamily: '"Open Sans", sans-serif',
      fontSmoothing: 'antialiased',
      '::placeholder': {
        color: '#CFD7DF',
      },
    },
    invalid: {
      color: '#e5424d',
      ':focus': {
        color: '#303238',
      },
    },
  };

// Mount the card element
let card = elements.create('card', { style: style });
card.mount('#card-element');

// display errors
card.on('change', function (event) {
  displayError(event);
});

function displayError(event) {
  // changeLoadingStatePrices(false);
  let displayError = document.getElementById('card-element-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
}

let form = document.getElementById('subscription-payment');

form.addEventListener('submit', function (ev) {
  ev.preventDefault();
  $('#subscribe-button').attr('disabled', true);
  $('#payment-content').fadeToggle(500);
  $('#payment-processing-overlay').fadeToggle(500);
  createPaymentMethod({ card });
});

// createPaymentMethod and createSubscription are based on
// official Stripe documentation
function createPaymentMethod({ card }) {
    const customerId = $('#id_customer_id').text().slice(1, -1);
    let billingName = $('#id_billing_name').text().slice(1, -1);  
    let billingEmail = $('#id_billing_email').text().slice(1, -1);    
    let priceId = $('#id_price_id').text().toUpperCase().slice(1, -1);
  
    stripe
      .createPaymentMethod({
        type: 'card',
        card: card,
        billing_details: {
          name: billingName,
          email: billingEmail,
        },
      })
      .then((result) => {
        if (result.error) {
          displayError(result);
        } else {
          createSubscription({
            customerId: customerId,
            paymentMethodId: result.paymentMethod.id,
            priceId: priceId,
          });
        }
      });
  }
  
function createSubscription({ customerId, paymentMethodId, priceId }) {
  let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  return (
    fetch('/memberships/create_subscription/', {
      method: 'post',
      headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': csrfToken,
      },
      body: JSON.stringify({
        customerId: customerId,
        paymentMethodId: paymentMethodId,
        priceId: priceId,
      }),
    })
      .then((response) => {
        return response.json();
      })
      // If the card is declined, display an error to the user.
      .then((result) => {
        if (result.error) {
          // The card had an error when trying to attach it to a customer.
          throw result;
        }
        return result;
      })
      // Normalize the result to contain the object returned by Stripe.
      // Add the additional details we need.
      .then((result) => {
        return {
          paymentMethodId: paymentMethodId,
          priceId: priceId,
          subscription: result,
        };
      })
      .then(onSubscriptionComplete)
      .catch((error) => {
        // An error has happened. Display the failure to the user here.
        // We utilize the HTML element we created.
        showCardError(error);
      })
  );
}

function onSubscriptionComplete(result) {
  // Payment was successful, redirect subscriber to dashboard
  if (result.subscription.status === 'active') {
    window.location.href = '/memberships/checkout_success';
  } else {
    window.location.href = '/memberships/signup';
  }
}
