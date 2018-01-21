from django.db import models

from django.db.models.signals import pre_save
from django.urls import reverse

from series.models import Series

from .utils import unique_slug_generator

class Episode(models.Model):
	series 		= models.ForeignKey(Series, default=True, on_delete=models.CASCADE)
	title 		= models.CharField(max_length=120, null=True, blank=True)
	ep_number 	= models.IntegerField(editable=False)
	updated		= models.DateField(auto_now=True)
	timestamp 	= models.DateField(auto_now_add=True)
	slug 		= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('episodes:detail', kwargs={'episode_slug':self.slug})

	def save(self):
		count = self.series.episode_set.count()
		self.ep_number = count + 1
		return super(Episode, self).save()

	class Meta:
		ordering = ['ep_number']


def pre_save_episode_receiver(sender, instance, *args, **kwargs):
	instance.slug = unique_slug_generator(instance)
	

pre_save.connect(pre_save_episode_receiver, sender=Episode)

