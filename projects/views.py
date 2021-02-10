from django.shortcuts import render
from .models import Project


def projects(request):
    """ A view to render Projects Page """

    projects = Project.objects.all().order_by('-date')

    template = 'projects/projects.html'
    context = {
        'projects': projects,
    }

    return render(request, template, context)
