from django.db import models
from django_markdown.models import MarkdownField

class ProgramQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class Program(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	short_description = models.CharField(max_length=1300)
	description = MarkdownField()

	objects = ProgramQuerySet.as_manager()

	def __unicode__(self):
		return self.name