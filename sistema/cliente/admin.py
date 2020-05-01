from django.contrib import admin

from .models import Cidade
from .models import Endereco
from .models import Cliente

# Register your models here.

admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(Cliente)