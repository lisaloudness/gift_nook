from django.shortcuts import render


def about_us(request):
    """ A view to return the about_us page """

    return render(request, 'about_us/about_us.html')

def ethos(request):
    """ A view to return the ethos page """

    return render(request, 'about_us/ethos.html')
