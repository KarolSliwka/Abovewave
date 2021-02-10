from django.shortcuts import render
from home.models import AuthorBlock


def info(request):
    """A view to render Info Page."""

    authors = AuthorBlock.objects.all()

    template = 'home/index.html'
    context = {
        'authors': authors,
    }

    return render(request, template, context)
