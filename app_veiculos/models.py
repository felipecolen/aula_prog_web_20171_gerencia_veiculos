
# python3.4 manage.py makemigrations
# python3.4 manage.py migrate

from django.db import models

# Create your models here.
class TipoDeVeiculo(models.Model):
    tipo = models.CharField('Tipo de Veículo', max_length=20,
                            help_text='Ex. Carro ou Moto')

    def __str__(self):
        return "{}".format(self.tipo)

    class Meta:
        ordering = ('tipo', )
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'


class MarcaDoVeiculo(models.Model):
    marca = models.CharField('Marca do Veículo',
                             max_length=20,
                             help_text='Ex. Nissan, Honda,'
                                       'Fiat')

    def __str__(self):
        return '{}'.format(self.marca)

    class Meta:
        ordering = ('marca', )
        verbose_name = 'Marca do Veículo'
        verbose_name_plural = 'Marcas dos Veículos'


class Veiculo(models.Model):
    tipo = models.ForeignKey(TipoDeVeiculo)
    marca = models.ForeignKey(MarcaDoVeiculo)

    modelo = models.CharField('Modelo', max_length=50)
    placa = models.CharField('Placa', max_length=8)
    cor = models.CharField('Cor', max_length=10)

    def __str__(self):
        return '{} - {}'.format(self.placa, self.modelo)

    class Meta:
        ordering = ('tipo', 'marca', 'modelo')
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'












