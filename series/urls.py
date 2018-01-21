from django.conf.urls import url, include

from .views import SeriesListView, SeriesDetailView, SeriesCreateView

urlpatterns = [
	url(r'^$', SeriesListView.as_view(), name = 'list'),
	url(r'^create/$', SeriesCreateView.as_view(), name='create'),
	url(r'^(?P<slug>[\w-]+)/$', SeriesDetailView.as_view(), name = 'detail'),
	# url(r'^(?P<slug>[\w-]+)/(?P<title>[\w-]+)$', EpisodeDetailView.as_view(), name='ep_detail'),
]