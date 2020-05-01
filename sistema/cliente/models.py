from django.db import models

# Create your models here.


class Cidade(models.Model):
	nm_cidade = models.CharField(max_length=20)
	nm_estado = models.CharField(max_length=15)
	sg_estado = models.CharField(max_length=2)
	nm_pais = models.CharField(max_length=10)
	sg_pais = models.CharField(max_length=3)

	def __str__(self):
		return self.nm_cidade + " - " + self.sg_estado

class Endereco(models.Model):
	tp_logradouro = models.CharField(max_length=15)
	nm_logradouro = models.CharField(max_length=40)
	nm_bairro = models.CharField(max_length=20)
	cd_cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

	def __str__(self):
		return self.tp_logradouro + " " + self.nm_logradouro + ", " + self.nm_bairro	


class Cliente(models.Model):
	nm_cliente = models.CharField(verbose_name="Nome do cliente", max_length=45)
	nm_mae = models.CharField(verbose_name="Nome da mãe", max_length=45, null=True, blank=True)
	email = models.EmailField(verbose_name="Email", max_length=45, default="Não informado")
	nr_cpf = models.CharField(verbose_name="Número do CPF", max_length=14)
	nr_rg = models.CharField(verbose_name="Número do RG", max_length=15)
	dt_nascimento = models.DateField(verbose_name="Data de nascimento")
	idade = models.IntegerField(verbose_name="Idade")
	nr_endereco = models.IntegerField(null=True, blank=True)
	dsc_complemento = models.TextField(null=True, blank=True)
	cd_endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)

	def __str__(self):
		return self.nm_cliente
	