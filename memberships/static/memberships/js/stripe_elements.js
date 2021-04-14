let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
console.log(stripePublicKey)
let clientSecret = $('#id_client_secret').text().slice(1, -1);
console.log(clientSecret)
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
let card = elements.create('card', { style: style });
card.mount('#card-element');

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

  var form = document.getElementById('subscription-form');

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
  });
  
  function createPaymentMethod({ card }) {
    const customerId = {{ CUSTOMER_ID }};
    // Set up payment method for recurring usage
    let billingName = document.querySelector('#name').value;
  
    let priceId = document.getElementById('priceId').innerHTML.toUpperCase();
  
    stripe
      .createPaymentMethod({
        type: 'card',
        card: card,
        billing_details: {
          name: billingName,
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