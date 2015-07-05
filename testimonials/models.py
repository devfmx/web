"""Testimonials models."""

from django.db import models


class Testimonial(models.Model):

    """Testimonial model."""

    testimonial = models.TextField(max_length=1000)
    person = models.CharField(max_length=255)
    person_title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='testimonials',
                                null=True, blank=True)

    def __unicode__(self):
        """Return the person name and person title."""
        return "%s %s" % (self.person, self.person_title)

    def ViewPicture(self):
        """Return a HTML with the testimonial person picture."""
        return """<img src="%s" style="
                  display: block; width: 50px;"/>
               """ % self.picture

    ViewPicture.allow_tags = True
