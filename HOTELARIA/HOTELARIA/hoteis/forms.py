from django import forms
from django.core.mail import send_mail
from django.conf import settings
from HOTELARIA.core.mail import send_mail_template
from .models import Hotel, Comentario
from django.contrib.auth import get_user_model

User = get_user_model()

class ContatoHotel(forms.Form):

	nome = forms.CharField(label = 'Nome', max_length=100) 
	email = forms.EmailField(label='E-mail')
	mensagem = forms.CharField(label="Mensagem/Dúvida", widget=forms.Textarea)

	def send_mail(self, hotel):
		
		assunto = '[%s] Contato' % hotel.nome
		contexto = {
			'nome':self.cleaned_data['nome'],
			'email':self.cleaned_data['email'],
			'mensagem':self.cleaned_data['mensagem'],

		}
		user = User.objects.get(pk = hotel.user_id)
		print('User')
		print(user.email)
		nome_template = 'contato_email.html'
		send_mail_template(assunto, nome_template, contexto, [hotel.email, user.email])

class PesquisaForm(forms.Form):
	pesquisa = forms.CharField(label = 'Pesquisa', max_length='150')

class AdicionarHotelForm(forms.ModelForm):
	class Meta:
		model = Hotel
		exclude = ['']

class ComentarioForm(forms.ModelForm):
	class Meta:
		model = Comentario
		exclude = ['']
