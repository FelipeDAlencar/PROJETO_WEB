from django.shortcuts import render



def home(request):
	nome_template = 'home.html'
	return render(request,nome_template)
def contato(request):
	nome_template = 'contato.html'
	return render(request, nome_template)