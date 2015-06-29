from django.db import models

class Mentor(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	short_description = models.CharField(max_length=1300, blank=True)