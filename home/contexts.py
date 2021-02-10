from datetime import datetime
from .models import SocialMediaIcon


def FooterContext(request):

    social_media = SocialMediaIcon.objects.all().order_by('name')
    currentYear = datetime.now().year

    context = {
        'social_media': social_media,
        'currentYear': currentYear,
    }

    return context
