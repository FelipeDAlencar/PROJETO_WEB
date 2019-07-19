from django.shortcuts import render, get_object_or_404
from .models import Hotel
from .forms import ContatoHotel, AdicionarHotelForm, PesquisaForm, ComentarioForm

def index(request):
	nome_do_template = 'index.html'
	hoteis = Hotel.objects.all()
	contexto = {'hoteis':hoteis}

	form = PesquisaForm(request.POST or None)
	if form.is_valid():
		contexto['sucesso'] = True
		pesquisa = request.POST['pesquisa']
		hoteis = Hotel.objects.buscar(pesquisa)
		contexto['hoteis'] = hoteis
		form = PesquisaForm()
		contexto['form'] = form
		return render(request, nome_do_template,contexto)
	else:
		form = PesquisaForm()
		contexto['form'] = form
		return render(request, nome_do_template,contexto)
	

def adicionarHotel(request):
	contexto = {}
	if request.method == 'POST':
		form = AdicionarHotelForm(request.POST)
		if(form.is_valid()):
			form.save()
			contexto['success'] = True
			form = AdicionarHotelForm()

	else:
		form = AdicionarHotelForm()

	contexto['form'] = form 
	nome_do_template = 'adicionarHotel.html'
	return render(request, nome_do_template, contexto)

def detalhes(request, slug):
	hotel = get_object_or_404(Hotel, slug=slug)
	contexto = {}
	form = ContatoHotel(request.POST or None)
	comentarioForm = ComentarioForm(request.GET or None)
	if request.method == 'POST':
		form = ContatoHotel(request.POST)
		if(form.is_valid()):
			contexto['is_valid'] = True
			form.send_mail(hotel)
			contexto['form'] = form 
			form = ContatoHotel()
	elif request.method == 'GET':
		comentarioForm = ComentarioForm(request.GET)
		if comentarioForm.is_valid():
			contexto['sucesso'] = True
			comentarioForm.save()
			comentarioForm = ComentarioForm()
	else:
		form = ContatoHotel()
		comentarioForm = ComentarioForm()

	contexto['form'] = form 
	contexto['hotel'] = hotel
	contexto['comentarios'] = hotel.comentarios.all()
	contexto['comentarioForm'] = comentarioForm

	nome_do_template = 'detalhes.html'
	return render(request, nome_do_template, contexto)










