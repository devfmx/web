from django.contrib import admin

from . import models

@admin.register(models.Mentor)
class MentorAdmin(admin.ModelAdmin):
	list_display = ('id', 'first_name', 'last_name', 'short_description')
	search_fields = ('first_name', 'last_name')