from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_veiculos.models import Veiculo
from app_veiculos.serializers import VeiculosSerializer


@api_view(['GET'])
def veiculos_todos(request):
    if request.method == 'GET':
        veiculos = Veiculo.objects.all()
        serializer = VeiculosSerializer(veiculos, many=True)
        return Response(serializer.data)

