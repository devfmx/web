from django.db import models

class Sensei(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=200, unique=True)
	specialty = models.CharField(max_length=600)
	short_description = models.CharField(max_length=600, blank=True, null=True)
	picture = models.ImageField(upload_to='senseis', blank=True, null=True)

	def __unicode__(self):
		return "%s %s" %(self.first_name, self.last_name)

	def show_picture(self):
		if self.picture:
			return """<img src="%s" style="display:block; width: 70px;" />""" %self.picture.url
		else:
			return self.picture

	show_picture.allow_tags = True