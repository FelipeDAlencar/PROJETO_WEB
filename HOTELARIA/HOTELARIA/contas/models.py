import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.conf import settings

class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField('Nome do usuário', max_length=30, unique=True,
	 validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'O nome de usuário pode conter apenas letras, digitos ou @/./+/-/',
	 'invalid')])

	email = models.EmailField('E-mail', unique=True)
	name = models.CharField('Nome completo', max_length=100, blank=True)
	is_active = models.BooleanField('Está ativo ?', blank=True, default =True)
	is_staff = models.BooleanField('É da administração ?', blank = True, default = False)
	date_joined = models.DateTimeField('Data de entrada', auto_now_add = True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return self.name or self.username

	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return __str__(self)

	class Meta:
		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

class ResetarSenha(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário',
		related_name='resetar'
		)
	key = models.CharField('Chave', max_length=100, unique=True)
	criada_em = models.DateTimeField('Data de criação', auto_now_add=True)
	confirmacao = models.BooleanField('confirmado?', default=False, blank=True)

	def __str__(self):
		return '{0} - {1}'.format(self.user, self.criada_em)

	class Meta():
		verbose_name = 'Nova Senha'
		verbose_name_plural = 'Novas senhas'
		ordering = ['-criada_em']
