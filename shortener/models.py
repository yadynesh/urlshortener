from django.db import models

# Create your models here.
from .utils import generateShortcode

class MagicUrl(models.Model):
	url = models.CharField(max_length = 220)
	shortcode = models.CharField(max_length = 20,unique = True, blank = True)
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)
	active = models.BooleanField(default = True)

	

	def save(self, *args, **kwargs):

		#Ensures code does not change every time you save
		if self.shortcode is None or self.shortcode == "" : 
			self.shortcode = generateShortcode(self)
		super (MagicUrl, self).save(*args, **kwargs)

	def __str__(self):
		return self.url


