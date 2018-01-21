from django.conf.urls import url

from .views import ProfileDetailView, FollowersListView, FollowingListView

urlpatterns = [
	url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='detail'),
	url(r'^(?P<username>[\w-]+)/followers/$', FollowersListView.as_view(), name='followers_list'),
	url(r'^(?P<username>[\w-]+)/following/$', FollowingListView.as_view(), name='following_list'),
]