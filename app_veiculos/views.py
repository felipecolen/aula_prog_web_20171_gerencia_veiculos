import urllib

import requests
from django.http.response import HttpResponse
from django.shortcuts import render
from app_veiculos.models import Veiculo


def index(request):

    consulta_no_banco = Veiculo.objects.all()

    return render(request, 'index.html',
                  {'consulta_no_banco': consulta_no_banco})


# exemplo de como capturar os dados
def teste_get_dados(request):
    url_da_api = 'http://localhost:8000/api/v1/veiculos/'
    dados_recebidos = requests.get(url_da_api)

    print('Dados recebidos = TEXTO')
    for d in dados_recebidos:
        print(d.upper())

    print('')
    print('Dados recebidos serializados = JSON')
    json = dados_recebidos.json()
    for j in json:
        print(j['id'], j['placa'])

    return HttpResponse(json)
