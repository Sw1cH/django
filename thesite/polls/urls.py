from django.conf.urls import patterns, url, include
from polls import views

urlpatterns = patterns ('',
	# /polls/
	url(r'^$', views.index, name='index'),
	# /polls/2
	url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),\
	# /polls/2/results
	url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
	# /polls/2/vote
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	) 