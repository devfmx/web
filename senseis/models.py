"""Senseis model module."""

from django.db import models


class Sensei(models.Model):

    """Sensei model."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    specialty = models.CharField(max_length=600)
    short_description = models.CharField(max_length=600, blank=True, null=True)
    picture = models.ImageField(upload_to='senseis', blank=True, null=True)
    picture2 = models.ImageField(upload_to='senseis', blank=True, null=True)

    def __unicode__(self):
        """Return the first and last name of the instance object."""
        return "%s %s" % (self.first_name, self.last_name)

    def show_picture(self):
        """Return a renderable HTML with the sensei image."""
        if self.picture:
            return """<img src="%s" style="display:block;
                       width: 70px;" />
                   """ % self.picture.url
        else:
            return self.picture

    def show_picture2(self):
        """Return a renderable HTML with the sensei image 2."""
        if self.picture2:
            return """<img src="%s" style="display:block;
                       width: 70px;" />
                   """ % self.picture2.url
        else:
            return self.picture2

    show_picture.allow_tags = True
    show_picture2.allow_tags = True
