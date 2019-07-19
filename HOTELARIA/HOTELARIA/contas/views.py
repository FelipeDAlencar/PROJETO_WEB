from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm,SetPasswordForm
from django.conf import settings
from .forms  import RegistroForm,ResetarSenhaForm,EditarContaForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .models import ResetarSenha
from HOTELARIA.hoteis.models import Hotel
from HOTELARIA.hoteis.forms import AdicionarHotelForm
User = get_user_model()


@login_required
def painel(request):

	nome_template = 'contas/painel.html'
	sucesso = False
	contexto = {}
	try:
		hotel = Hotel.objects.get(user_id=request.user.id)
		sucesso = True		
		contexto['hotel'] = hotel

	except:	
		sucesso = False

	contexto['sucesso'] = sucesso
	return render(request, nome_template, contexto)

def registro(request):
	nome_template = 'contas/registro.html'

	if request.method == 'POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username = user.username, password= form.cleaned_data['password1'])
			login(request, user)
			return redirect('core:home')

	else:
		form = RegistroForm()
	contexto = {
		'form': form 
	}
	return render(request, nome_template, contexto)
	
def resetarSenha(request):
	nome_template = 'contas/resetarSenha.html'
	contexto = {}
	form = ResetarSenhaForm(request.POST or None)
	if form.is_valid():
		key = form.save()
		contexto['success'] = True
		contexto['key'] = key 

	contexto['form'] = form
	return render(request,nome_template, contexto)

def resetarSenhaConfirmacao(request, key):
	nome_template = 'contas/resetarSenhaConfirmacao.html'
	reset = get_object_or_404(ResetarSenha, key=key)
	contexto = {'reset':reset}
	form = SetPasswordForm(user=reset.user, data=request.POST or None)

	if form.is_valid():
		form.save()
		contexto['success'] = True
	contexto['form'] = form;
	return render(request,nome_template, contexto)

@login_required
def editar(request):
	contexto = {}
	nome_template = "contas/editarConta.html";

	if request.method == 'POST':
		form = EditarContaForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			form = EditarContaForm(instance=request.user)
			contexto['success'] = True
	else:
		form = EditarContaForm(instance=request.user)
	
	contexto['form'] = form
	return render(request, nome_template, contexto)

@login_required
def editarSenha(request):
	nome_template = 'contas/editarSenha.html'
	contexto = {}

	if request.method == 'POST':
		form =PasswordChangeForm(data = request.POST, user=request.user)
		if form.is_valid():
			form.save()
			contexto['success'] = True
	else:
		form = PasswordChangeForm(user=request.user)

	contexto['form'] = form
	return render(request, nome_template, contexto)

def atualizarHotel(request, id):
	hotel = Hotel.objects.get(id = id)
	nome_template = 'contas/editarHotel.html'
	contexto = {}
	form = AdicionarHotelForm(request.POST or None, instance =  hotel)
	if form.is_valid():
		form.save()
		contexto['sucesso'] = True
		return render(request, nome_template,contexto)

	else:
		contexto['form'] = form
		contexto['hotel'] = hotel
		return render(request, nome_template,contexto)


