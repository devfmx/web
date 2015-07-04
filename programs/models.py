"""Programs Model."""

from django.db import models
from django_markdown.models import MarkdownField


class ProgramQuerySet(models.QuerySet):

    """Class to add custom querysets to Program Model."""

    def published(self):
        """Get only the published programs."""
        return self.filter(publish=True)


class Program(models.Model):

    """Porgram Model."""

    name = models.CharField(max_length=255)
    old_price = models.FloatField(default=0.0)
    actual_price = models.FloatField(default=0.0)
    requirements = models.TextField(default='', null=True)
    logo = models.ImageField(upload_to='program_images', null=True)
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    short_description = models.CharField(max_length=1300)
    description = MarkdownField()

    objects = ProgramQuerySet.as_manager()

    def __unicode__(self):
        """Return the name when instance the class."""
        return self.name
