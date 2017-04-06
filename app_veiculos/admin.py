from django.contrib import admin

# Register your models here.
from app_veiculos.models import TipoDeVeiculo, Veiculo, MarcaDoVeiculo

admin.site.register(TipoDeVeiculo)
admin.site.register(MarcaDoVeiculo)
admin.site.register(Veiculo)
