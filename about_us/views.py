from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import render


def about_us(request):
    """ A view to return the about_us page """

    return render(request, 'about_us/about_us.html')


def ethos(request):
    """ A view to return the ethos page """

    return render(request, 'about_us/ethos.html')


def privacy(request):
    """ A view to return the privacy page """

    return render(request, 'about_us/privacy.html')
