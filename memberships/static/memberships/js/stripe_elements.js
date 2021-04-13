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
let card = elements.create('card', { style: style });
card.mount('#card-element');

// card.addEventListener('change', function (event) {
//     var errorDiv = document.getElementById('card-element-errors');
//     if (event.error) {
//         var html = `
//             <span class="icon" role="alert">
//                 <i class="fas fa-times"></i>
//             </span>
//             <span>${event.error.message}</span>
//         `;
//         $(errorDiv).html(html);
//     } else {
//         errorDiv.textContent = '';
//     }
// });

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