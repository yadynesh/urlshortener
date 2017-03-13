from django.db import models
from shortener.models import MagicUrl
# Create your models here.

class ClickEventManager(models.Manager):
	def create_event(self, instance):
		if isinstance(instance, MagicUrl): #here we send the object and check if it is MagicUrl object
			obj, create = self.get_or_create(magic_url = instance)
			obj.count += 1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	magic_url = models.OneToOneField(MagicUrl)
	#because of this we can directly call count using object of MagicUrl
	count = models.IntegerField(default = 0)
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)

	objects = ClickEventManager()

	def __str__(self):
		return str(self.magic_url) + "-" + str(self.count)