from django.db import models
from django.conf import settings
from .utils import generateShortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15) #'SHORTCODE_MAX' = 15 if SHORTCODE_MAX not specified in settings

class MagicUrlManager(models.Manager):
	def all(self, *args, **kwargs):
		qs = super (MagicUrlManager, self).all(*args, **kwargs)
		qs = qs.filter(active = True)
		return qs

	def refresh_shortcodes(self, items = None):
		print(self)
		qs = MagicUrl.objects.filter(id__gte = 1) #gte is greater than equal

		if items != None and isinstance(items, int):
			qs = qs.order_by('-id')[:items]
			new_codes = 0
			for q in qs:
				q.shortcode = generateShortcode(q)
				print(q.id)
				q.save()
				new_codes += 1
		return "Number of codes updated :{i}".format(i = new_codes)



class MagicUrl(models.Model):
	url = models.CharField(max_length = 220)
	shortcode = models.CharField(max_length = SHORTCODE_MAX,unique = True, blank = True)
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)
	active = models.BooleanField(default = True)

	objects = MagicUrlManager()
	#custom_objects = MagicUrlManager() 
	'''	incase you dont want to change the default objects.
		objects is an instance of Manager class.What we are doing is oveririding the Manager class and creating object of 
		the overridden class i.e MagicUrlManager
	'''

	# class Meta:
	# 	ordering = ['-id']
	
	def save(self, *args, **kwargs):

		#Ensures code does not change every time you save
		if self.shortcode is None or self.shortcode == "" : 
			self.shortcode = generateShortcode(self)
		super (MagicUrl, self).save(*args, **kwargs)

	def __str__(self):
		return self.url + "--" + self.shortcode


