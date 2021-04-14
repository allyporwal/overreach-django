// set up Stripe keys and style
let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
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
  changeLoadingStatePrices(false);
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
});

// $(document).ready(function() {
//   let billingName = $('#id_billing_name').text().slice(1, -1);
//   let priceId = $('#id_price_id').text().toUpperCase().slice(1, -1);
//   console.log(priceId)
// });

function createPaymentMethod({ card }) {
  const customerId = $('#id_customer_id').text().slice(1, -1);

  // Set up payment method for recurring usage
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
