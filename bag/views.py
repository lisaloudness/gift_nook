from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages

# Create your views here.

def view_bag(request):
    """Bag contents view """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    
    if item_id in bag:
        bag.pop(item_id)  # Remove the item from the bag
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)