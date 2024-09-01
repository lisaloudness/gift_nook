from django.shortcuts import render


def faq(request):
    """ A view to return the faqs page """

    return render(request, 'faq/faq.html')
