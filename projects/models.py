from django.db import models
from django.utils import timezone
from offer.models import OfferCategory


class Project(models.Model):
    """Project Model for Projects App."""
    image_main = models.ImageField(
        upload_to="images/projects", null=True, blank=True)
    image_side = models.ImageField(
        upload_to="images/projects", null=True, blank=True)
    image_bottom = models.ImageField(
        upload_to="images/projects", null=True, blank=True)
    name = models.CharField(max_length=256, null=False, blank=False)
    category = models.ForeignKey(
        OfferCategory, null=True, blank=False, on_delete=models.PROTECT)
    url = models.URLField(max_length=1024, default='', null=True, blank=True)
    date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.name
