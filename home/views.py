from django.shortcuts import render
from info.models import Info


def home(request):
    """ A view to render Home Page """

    information = Info.objects.all()

    template = 'info/info.html'
    context = {
        'information': information,
    }

    return render(request, template, context)
