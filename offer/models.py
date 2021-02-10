"""Module to create categories and offer models."""
from django.db import models


class OfferCategory(models.Model):
    """Categories for Offer Model."""
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=256, null=False, blank=False)
    friendly_name = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.friendly_name


class Offer(models.Model):
    """Offer Model."""
    category = models.ForeignKey(
        'OfferCategory', null=True, blank=False, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="images/offer", null=True, blank=True)
    name = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
