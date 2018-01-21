from django.shortcuts import render

from django.views.generic import View, ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Profile

class ProfileDetailView(DetailView):
	def get_object(self):
		username = self.kwargs.get('username')
		obj = get_object_or_404(Profile, user__username__iexact=username)
		return obj
	def get_context_data(self, *args, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		profile = context['object']
		series = profile.series.all()
		context["series_set"] = series
		print('serfegeth', series)
		return context

class FollowersListView(ListView):
	template_name = 'profiles/followers.html'
	def get_queryset(self):
		username = self.kwargs.get('username')
		profile  = Profile.objects.get(user__username__iexact=username)
		return profile.followers.all()

class FollowingListView(ListView):
	template_name = 'profiles/following.html'
	def get_queryset(self):
		username = self.kwargs.get('username')
		profile = Profile.objects.get(user__username__iexact=username)
		user = profile.user
		return user.following.all()


