from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^entrar/$', 'django.contrib.auth.views.login', 
		{'template_name': 'contas/login.html'}, name='login'),

	url(r'^sair/$', 'django.contrib.auth.views.logout', 
		{'next_page': 'core:home'}, name='logout'), 

	url(r'^$', 'HOTELARIA.contas.views.painel', name='painel'), 	

	url(r'^atualizar_hotel/(?P<id>\d+)/$', 'HOTELARIA.contas.views.atualizarHotel', name='atualizarHotel'), 	


	url(r'^cadastre-se/$', 'HOTELARIA.contas.views.registro', name='registro'),	

	url(r'^resetar_senha/$', 'HOTELARIA.contas.views.resetarSenha', name='resetarSenha'),

	url(r'^resetar_senha_confirmacao/(?P<key>\w+)/$', 'HOTELARIA.contas.views.resetarSenhaConfirmacao', name='resetarSenhaConfirmacao'),

	url(r'^editar/$', 'HOTELARIA.contas.views.editar', name='editar'),

	url(r'^editarSenha/$', 'HOTELARIA.contas.views.editarSenha', name='editarSenha'), 
    
)