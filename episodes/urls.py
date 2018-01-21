from django.conf.urls import url

from .views import EpisodeDetailView

urlpatterns = [
	url(r'^(?P<episode_slug>[\w-]+)/$', EpisodeDetailView.as_view(), name='detail')
]