"""Testimonials models."""

from django.db import models


class Testimonial(models.Model):

    """Testimonial model."""

    testimonial = models.TextField(max_length=1000)
    person = models.CharField(max_length=255)
    person_title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='senseis',
                                null=True, blank=True)

    def __unicode__(self):
        """Return the person name and person title."""
        return "%s %s" % (self.person, self.person_title)

    def ViewPicture(self):
        """Return a HTML with the testimonial person picture."""
        if self.picture.url:
            return """<img src="%s" style="
                      display: block; width: 50px;"/>
                   """ % self.picture.url
        else:
            return None

    ViewPicture.allow_tags = True


class Press(models.Model):

    """Press model."""

    quoute = models.CharField(max_length=255, null=True, blank=True)
    press_namme = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='press', null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        """Return the press name."""
        return self.press_namme

    def showImage(self):
        """Return a HTML with the press picture."""
        if self.image.url:
            return """<img src="%s" style="
                      display: block; width: 50px;"/>
                   """ % self.image.url
        else:
            return None
