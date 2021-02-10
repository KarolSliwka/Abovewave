from django.contrib import admin
from .models import Info, InfoLineItem


class AdminInfoLineItem(admin.StackedInline):
    model = InfoLineItem
    extra = 1

class AdminInfo(admin.ModelAdmin):
    """"""
    list_display = (
        'name',
        'image',
    )

    inlines = [ AdminInfoLineItem ]

    ordering = ('name',)

admin.site.register(Info, AdminInfo)