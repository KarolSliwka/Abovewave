""" Home App Models """
from django.db import models


class AuthorBlock(models.Model):
    """ Author main page block """
    name = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to="images/author", null=True, blank=True)
    about = models.TextField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class SocialMediaIcon(models.Model):
    """ Footer social media icons """
    name = models.CharField(max_length=150, null=True, blank=False)
    image = models.ImageField(
        upload_to="images/socials", null=True, blank=True)
    social_url = models.URLField(max_length=1024, default='', null=True, blank=True)

    def __str__(self):
        return self.name
