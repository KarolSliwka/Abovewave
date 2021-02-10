from django.contrib import admin
from .models import Project


class AdminProject(admin.ModelAdmin):
    """ Project Model Registerd to Admininistartion """
    list_display = (
        'name',
        'category',
        'image_main',
        'image_side',
        'image_bottom',
        'description',
    )

    ordering = ('name',)


admin.site.register(Project, AdminProject)
