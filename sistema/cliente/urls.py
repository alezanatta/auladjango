from django.urls import path

from . import views


app_name = "cliente"

urlpatterns = [
	path("", views.index, name="index"),
	path("hora/", views.hora, name="hora"),
	path("abacate/", views.abacate, name="abacate"),
	path("cidade/", views.cidadeView, name="cidade"),
	path("endereco/", views.enderecoView, name="endereco"),
	path("cadastro/", views.clienteCadastro, name="cadastro"),
	path("busca/", views.clienteBusca, name="busca"),
	#path("cadastra/", views.cadastra, name="cadastra"),
]