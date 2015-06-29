from django.contrib import admin

from . import models

from django_markdown.admin import MarkdownModelAdmin

@admin.register(models.Program)
class ProgramAdmin(MarkdownModelAdmin):
	list_display = ('name', 'slug', 'publish', 'modified', 'created')
	search_fields = ('slug', 'name')
	prepopulated_fields = {'slug': ('name',)}