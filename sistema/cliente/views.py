from django.shortcuts import render

from django.http import HttpResponse, Http404
from datetime import datetime

#Formulários
from .forms import CidadeForm
from .forms import EnderecoForm
from .forms import ClienteForm

#Models
from .models import Cliente

# Create your views here.


def index(request):
	return render(request, "cliente/index.html", {})

def hora(request):

	context = {"hora":datetime.now()}

	return render(request, "cliente/hora.html", context)

def abacate(request):
	nome = "Abacate"
	dtNascimento = "01/04/2020"
	cor = "verde"
	status = "maduro"
	cpf = "12"
	rg = "14"

	context = {
		"nome":nome,
		"dtNascimento":dtNascimento,
		"cor":cor,
		"status":status,
		"cpf":cpf,
		"rg":rg
	}

	return render(request, "cliente/abacate.html", context)

def cidadeView(request):

	if request.method == "GET":
		form = CidadeForm()
		context = {"form":form}
		return render(request, "cliente/cidade.html", context)
	elif request.method == "POST":
		pass

def enderecoView(request):

	form = EnderecoForm()

	context = {"form":form}

	return render(request, "cliente/endereco.html", context)

#Cadastro de clientes
def clienteCadastro(request):
	
	context = {}
	form = ClienteForm()
	context["form"] = form

	if request.method == "POST":
		resultado = ClienteForm(request.POST)
		if resultado.is_valid():
			resultado.save()
			sucesso = "Cliente salvo com sucesso"
			context["sucesso"] = sucesso
		else:
			erro = "Cliente não foi salvo"
			context["erro"] = erro

	return render(request, "cliente/cliente.html", context)

#Buscar clientes
def clienteBusca(request):
	
	clientes = Cliente.objects.all()
	
	context = {"clientes":clientes}
	#context = {}

	return render(request, "cliente/buscaCliente.html", context)


def cadastra(request):
	pass