import json
import time
import requests

from django.http import HttpResponse
from django.shortcuts import render, redirect

from registration.views import ActivationView


class MyActivationView(ActivationView):
    def get_success_url(self, user):
        return '/profile/'


def index(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'main/index.html', {})


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


def nutrition(request):
    food_group = {
        'A': {
            'name': 'Alimentos de origen animal',
            'energy': 40,  # kcal
            'carbohydrates': 0,  # grames
            'fat': 1,  # grames
            'protein': 7,  # grames
        },
        'Az': {
            'name': 'Azúcares',
            'energy': 40,  # kcal
            'carbohydrates': 10,  # grames
            'fat': 0,  # grames
            'protein': 0,  # grames
        },
        'CT': {
            'name': 'Cereales y Tubérculos',
            'energy': 70, # kcal
            'carbohydrates': 15, # grames
            'fat': 0, # grames
            'protein': 2, # grames
        },
        'F': {
            'name': 'Frutas',
            'energy': 60,  # kcal
            'carbohydrates': 15,  # grames
            'fat': 0,  # grames
            'protein': 0,  # grames
        },
        'G': {
            'name': 'Grasas',
            'energy': 70,  # kcal
            'carbohydrates': 3,  # grames
            'fat': 5,  # grames
            'protein': 3,  # grames
        },
        'L': {
            'name': 'Leguminosas',
            'energy': 120,  # kcal
            'carbohydrates': 20,  # grames
            'fat': 1,  # grames
            'protein': 8,  # grames
        },
        'LE': {
            'name': 'Alimentos libres de energía',
            'energy': 70,  # kcal
            'carbohydrates': 15,  # grames
            'fat': 0,  # grames
            'protein': 2,  # grames
        },
        'LS': {
            'name': 'Leche y Sustitutos',
            'energy': 150,  # kcal
            'carbohydrates': 12,  # grames
            'fat': 8,  # grames
            'protein': 9,  # grames
        },
        'V': {
            'name': 'Vegetales',
            'energy': 25,  # kcal
            'carbohydrates': 4,  # grames
            'fat': 0,  # grames
            'protein': 2,  # grames
        },
    }
    weight = {
        'normal': {'f': (1600, 1800), 'm': (1800, 2000)},
        'overweight': {'f': (1200, 1400), 'm': (1400, 1600)},
    }
    diets = {
        # n kcal: {food group: portion}
        1000: {'CT': 1, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
        1200: {'CT': 2, 'V': 1, 'F': 1, 'LE': 1, 'G': 1},
        1400: {'CT': 2, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
        1600: {'CT': 2, 'V': 2, 'F': 1, 'LS': 1, 'G': 1},
        1800: {'CT': 3, 'V': 1, 'F': 2, 'A': 1, 'LS': 1, 'G': 1},
        2000: {'CT': 3, 'V': 1, 'F': 2, 'A': 2, 'LS': 1, 'G': 1},
    }

    height = 1.7
    weight = 70
    imc = weight / height**2
    print(imc)

    if imc < 18.5:
        status = 'Desnutrición'
    elif imc < 25:
        status = 'Normal'
    elif imc < 30:
        status = 'Sobrepeso'
    else:
        status = 'Obesidad'

    return HttpResponse(status)
