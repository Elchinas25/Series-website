from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import pre_save
from django.urls import reverse

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

class Series(models.Model):
	owner 		= models.ForeignKey(User)
	title 		= models.CharField(max_length=120, blank=False, null=False)
	creator 	= models.CharField(max_length=120, blank=False, null=False)
	productor 	= models.CharField(max_length=120, blank=False, null=False)
	slug 		= models.SlugField(null=True, blank=True)
	rating 		= models.IntegerField()
	released	= models.DateField(null=True)


	class Meta:
		ordering = ['-rating']


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('series:detail', kwargs={'slug': self.slug})

def pre_save_series_receiver(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance, new_slug=None)

pre_save.connect(pre_save_series_receiver, sender = Series)
