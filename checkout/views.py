from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PK4CmP0P0tql3iAF2kVS0UTFdkWT128ZJYovYpVy30Y89n8rhp13IgPo71bRMvW4GGKzefsINUnfDt92zzdtxIE00WFmfNu10',
        'client_secret': 'sk_test_51PK4CmP0P0tql3iAheQIx2ISDOowEprRfIIzudx61uuPn1L3VUDJ8XSHKi7i4IXl1FZvnM5Dd4Gl1MWJxTJo7K2n00GmSfeB9f',
    }   


    return render(request, template, context)
