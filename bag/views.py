from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """Bag contents view """

    return render(request, 'bag/bag.html')
