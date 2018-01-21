from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView

from .models import Episode

class EpisodeDetailView(DetailView):
	template_name = 'episodes/episode_detail.html'
	# def get_queryset(self):
	# 	episode_slug = self.kwargs.get('episode_slug')
	# 	print(episode_slug)
	# 	qs = Episode.objects.filter(slug__iexact=episode_slug)
	# 	return qs
	def get_object(self):
		episode_slug = self.kwargs.get('episode_slug')
		print('Hola nene', episode_slug)
		obj = get_object_or_404(Episode, slug__iexact=episode_slug)
		# obj = Episode.objects.filter(slug=episode_slug)[0] #Both work!
		print(obj)
		return obj
	

	

