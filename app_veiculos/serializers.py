from rest_framework import serializers
from app_veiculos.models import Veiculo


class VeiculosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Veiculo
        fields = ('id', 'tipo', 'marca', 'modelo', 'placa', 'cor')
