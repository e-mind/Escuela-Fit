import json
import time
import requests

from django.http import HttpResponse


def weather(request):
    url = 'https://pacific-garden-86188.herokuapp.com/estacion'
    date = time.strftime("%Y-%m-%d", time.localtime())
    param = 'CO'
    station = 144
    range = 4
    payload = {'estacion': station, 'Fecha': date, 'parametro': param, 'rango': range}

    response = requests.get(url, params=payload)
    response = json.loads(response.text)
    response = response.pop()

    response = 'No realizar actividad física' if float(response['valor']) > 1 else 'Clima apto para la actividad física'

    return HttpResponse(response)
