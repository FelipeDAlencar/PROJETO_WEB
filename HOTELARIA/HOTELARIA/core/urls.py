from django.conf.urls import patterns, include, url

urlpatterns = patterns('HOTELARIA.core.views',
	url(r'^$', 'home', name='home'),
	url(r'^contato/$', 'contato', name='contato'),
    
)