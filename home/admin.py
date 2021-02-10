from django.contrib import admin
from .models import SocialMediaIcon, AuthorBlock


class AdminAuthorBlock(admin.ModelAdmin):
    """  """
    list_display = (
        'name',
        'image',
        'about',
    )

    ordering = ('name',)

class AdminSocialMediaIcons(admin.ModelAdmin):
    """  """
    list_display = (
        'name',
        'image',
        'social_url',
    )

    ordering = ('name',)


admin.site.register(AuthorBlock, AdminAuthorBlock)
admin.site.register(SocialMediaIcon, AdminSocialMediaIcons)

