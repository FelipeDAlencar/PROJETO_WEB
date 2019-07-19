from django import forms
from django.contrib.auth import get_user_model
from HOTELARIA.core.utils import generate_hash_key
from HOTELARIA.core.mail import send_mail_template
from django.contrib.auth import get_user_model
from .models import ResetarSenha

User = get_user_model()

class ResetarSenhaForm(forms.Form):
	email = forms.EmailField(label='E-mail')

	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			return email
		raise forms.ValidationError('Nenhum usuário encontrado com este endereço de e-mail')
	def save(self):
		user = User.objects.get(email=self.cleaned_data['email'])
		key = generate_hash_key(user.username)
		resetar = ResetarSenha(user=user, key=key)
		resetar.save()
		template_name = 'contas/resetarSenhaMail.html'
		subject = 'Criar nova senha no HOTELARIA'
		contexto = {'resetar':resetar}
		send_mail_template(subject, template_name, contexto, [user.email])
		return key


class RegistroForm(forms.ModelForm):
	password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
		 	raise forms.ValidationError('A confirmação de senha não está correta', )
		return password2

	def save(self, commit=True):
		user = super(RegistroForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user
	class Meta():
		model = User
		fields = ['username','email']
		
class EditarContaForm(forms.ModelForm):
	class Meta():
		model = User
		fields = ['username','email']