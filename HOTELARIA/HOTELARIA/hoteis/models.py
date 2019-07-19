from django.db import models
from django.conf import settings

class HotelManager(models.Manager):

	def buscar(self, query):
		return self.get_queryset().filter(models.Q(nome__icontains=query) | models.Q(descricao__icontains=query) |
			models.Q(cidade__icontains=query) | models.Q(rua__icontains=query))


class Hotel(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário',
		related_name='usuario_hotel'
		)
	nome = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	descricao = models.TextField('Descricao')
	telefone = models.CharField('Telefone', max_length=100)
	cidade = models.CharField('Cidade', max_length=100)
	rua = models.CharField('Rua', max_length=100)
	bairro = models.CharField("Bairro", max_length=100)
	numero = models.PositiveIntegerField("Número")
	imagem = models.ImageField(upload_to='hotel/imagens', verbose_name='Imagem', null=True, blank=True)
	email = models.EmailField('E-mail', null = True, blank=True, unique = True)
	criado_em = models.DateTimeField('Criando em', auto_now_add = True)
	atualizado_em = models.DateTimeField('Atualizado em', auto_now = True)

	objects = HotelManager()

	@models.permalink
	def get_absolute_url(self):
		return ('hoteis:detalhes', (), {'slug':self.slug})
	def __str__(self):
		return self.nome

	class Meta:
		ordering = ['nome']
		verbose_name = 'Hotél'
		verbose_name_plural = 'Hotéis'
		unique_together = (('user',))

class Comentario(models.Model):

	hotel = models.ForeignKey(Hotel, verbose_name='Hotél', related_name='comentarios')
	comentario = models.TextField('Comentario')
	nome = models.CharField('Nome', max_length = 100)
	criado_em = models.DateTimeField('Criando em', auto_now_add = True)
	atualizado_em = models.DateTimeField('Atualizado em', auto_now = True)

	def __str__(self):
		return self.nome
	

	class Meta:
		verbose_name = 'Comentário'
		verbose_name_plural = 'Comentários'
		ordering = ['criado_em']
