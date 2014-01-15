from django.conf.urls import patterns, url, include
from polls import views

urlpatterns = patterns ('',
	# /
	url(r'^$', views.index, name='index'),
	# /2
	url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),\
	# /2/results
	url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
	# /2/vote
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	) 