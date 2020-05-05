from django import forms
from django.forms import ModelForm

from django.utils.translation import gettext_lazy as _

from .models import Cidade
from .models import Endereco
from .models import Cliente

class CidadeForm(ModelForm):
	class Meta:
		model = Cidade
		fields = ["nm_cidade", "nm_estado", "nm_pais"]

		help_texts = {
			"nm_estado":_("Favor nome completo"),
			"nm_pais":_("Favor nome completo"),
		}

		labels = {
			"nm_cidade": "Nome da cidade",
			"nm_estado": "Nome do estado",
			"nm_pais": "Nome do país",
		}

		error_messages = {
			"nm_cidade":{
				"max_length":"Nome da cidade muito longo",
				"required":"Campo obrigatório",
			},
			"nm_estado":{
				"max_length":"Nome da cidade muito longo",
				"required":"Campo obrigatório",
			}
		}

class EnderecoForm(ModelForm):
	class Meta:
		model = Endereco
		fields = "__all__"

class ClienteForm(ModelForm):
	class Meta:
		model = Cliente
		fields = "__all__"

class BuscaClienteForm(forms.Form):
	nm_cliente = forms.CharField(max_length=45)
	dt_nascimento = forms.CharField(max_length=10)
	email = forms.EmailField(required=False)