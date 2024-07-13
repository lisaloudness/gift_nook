from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.context import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PK4CmP0P0tql3iAF2kVS0UTFdkWT128ZJYovYpVy30Y89n8rhp13IgPo71bRMvW4GGKzefsINUnfDt92zzdtxIE00WFmfNu10',
        'client_secret': 'sk_test_51PK4CmP0P0tql3iAheQIx2ISDOowEprRfIIzudx61uuPn1L3VUDJ8XSHKi7i4IXl1FZvnM5Dd4Gl1MWJxTJo7K2n00GmSfeB9f',
    }   


    return render(request, template, context)
