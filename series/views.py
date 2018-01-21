from django.shortcuts import render

from django.views.generic import View, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from django.shortcuts import redirect

from django.contrib.auth import get_user_model

User = get_user_model()

from .models import Series
from episodes.models import Episode
from .forms import SeriesModelForm

class SeriesListView(ListView):
	def get_queryset(self):
		return Series.objects.all()
	def get_context_data(self, *args, **kwargs):
		context = super(SeriesListView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get("query")
		qs = Series.objects.all()
		is_valid = True
		if query:
			qs = Series.objects.filter(title__iexact=query)
			if len(qs) == 0:
				is_valid = False
				qs = Series.objects.all()
		context["qs"] = qs
		context["is_valid"] = is_valid
		return context

class SeriesDetailView(DetailView):
	def get_queryset(self):
		return Series.objects.all()
	def get_context_data(self, *args, **kwargs):
		context = super(SeriesDetailView, self).get_context_data(*args, **kwargs)
		query = self.request.GET.get("episode_query")
		obj = kwargs["object"]
		is_valid = True
		episodes_set = obj.episode_set.all()
		if query:
			try:
				query = int(query)
				episodes_set = obj.episode_set.filter(ep_number=query)
			except:
				episodes_set = obj.episode_set.filter(
					Q(title__iexact=query) |
					Q(title__icontains=query) |
					Q(title__istartswith=query) |
					Q(title__iendswith=query) 
					)
			if len(episodes_set) == 0:
				is_valid = False
				episodes_set = obj.episode_set.all()

		profiles_associated = obj.profiles.all()
				
		context["is_valid"] = is_valid
		context["episodes_set"] = episodes_set
		context["profiles"] = profiles_associated

		return context


class SeriesCreateView(CreateView):
	form_class = SeriesModelForm
	success_url = '/series/'
	template_name = 'series/series_create.html'
	def form_valid(self, form):
		obj = form.save()
		return super().form_valid(form)
	def get_context_data(self, *args, **kwargs):
		context = super(SeriesCreateView, self).get_context_data(*args, **kwargs)
		context["model_var"] = 'Series'
		return context







# class EpisodeDetailView(DetailView):
# 	template_name = 'series/episode_detail.html'
# 	# def get_queryset(self):
# 		# series_obj.episode_set.all()
# 		# series_obj = kwargs["series"]
# 		# return Episode.objects.all()
# 	def get_object(self, *args, **kwargs):
# 		print(kwargs)
# 		qs = Episode.objects.all()
# 		ep_title = 'naruto'
# 		obj = Episode.objects.get(title__iexact=ep_title)
# 		return obj
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(EpisodeDetailView, self).get_context_data(*args, **kwargs) 
# 		print(kwargs)
# 		return context





