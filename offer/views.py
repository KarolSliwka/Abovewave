from django.shortcuts import render
from .models import Offer, OfferCategory


def offer(request):
    """A view to render Offer Page."""

    categories = OfferCategory.objects.all()
    offers = Offer.objects.all()

    template = 'offer/offers.html'
    context = {
        'categories': categories,
        'offers': offers,
    }

    return render(request, template, context)