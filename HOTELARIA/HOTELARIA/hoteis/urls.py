from django.conf.urls import patterns, include, url

urlpatterns = patterns('HOTELARIA.hoteis.views',
	url(r'^$', 'index', name='index'),
	url(r'^adicionar_hotel/$', 'adicionarHotel', name='adicionarHotel'),
	url(r'^(?P<slug>[\w_-]+)/$', 'detalhes', name='detalhes'),   
	
    
)