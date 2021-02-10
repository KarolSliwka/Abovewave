from django.contrib import admin
from .models import OfferCategory, Offer


class AdminOfferCategory(admin.ModelAdmin):
    """"""
    list_display = (
        'name',
        'friendly_name',
    )

    ordering = ('name',)

class AdminOffer(admin.ModelAdmin):
    """"""
    list_display = (
        'name',
        'category',
        'description',
    )

    ordering = ('name',)


admin.site.register(OfferCategory, AdminOfferCategory)
admin.site.register(Offer, AdminOffer)

