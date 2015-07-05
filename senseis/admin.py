"""Admin module for senseis."""

from django.contrib import admin

from . import models


@admin.register(models.Sensei)
class SenseiAdmin(admin.ModelAdmin):

    """Sensei Model Admin."""

    list_display = (
        'id',
        'first_name',
        'last_name',
        'specialty',
        'short_description',
        'show_picture',
        'show_picture2'
    )
    search_fields = ('slug', 'first_name', 'last_name')
    prepopulated_fields = {'slug': ('first_name',)}
