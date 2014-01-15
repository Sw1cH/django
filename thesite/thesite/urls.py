from django.conf.urls import patterns, include, url
from polls import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('polls.urls', namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^i18n/', include('django.conf.urls.i18n')),
)
