import datetime
import json
import os
import requests
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.physical_record.models import PhysicalRecord


def activation_complete(request):
    if request.user.is_authenticated:
        return redirect('index')


def index(request):
    if request.user.is_anonymous:
        return render(request, 'main/index.html', {})
    elif request.user.is_authenticated and hasattr(request.user, 'student'):
        return redirect('profile')
    else:
        return redirect('students:create')


@login_required
def profile(request):
    data_graphs = []
    record = PhysicalRecord.objects.filter(student=request.user.student)
    graphs = ['weightGraph', 'waistGraph', 'heartGraph']
    label = ['PESO', 'CIRCUNFERENCIA CINTURA', 'FRECUENCIA CARDIACA']
    bg_colors = ['#D4E6F1', '#A9DFBF', '#F9E79F']
    border_colors = ['#336699', '#239B56', '#F4D03F']
    texts = ['REGISTRO DE PESO', 'REGISTRO DE CIRCUNFERENCIA', 'REGISTRO DE FRECUENCIA']
    for i in range(3):
        labels = []
        data = []
        for r in record:
            if i == 0 and r.weight:
                labels.append(r.date.strftime("%d/%m/%y"))
                data.append(float(r.weight))
            if i == 1 and r.waist_circumference:
                labels.append(r.date.strftime("%d/%m/%y"))
                data.append(float(r.waist_circumference))
            if i == 2 and r.resting_heart_rate:
                labels.append(r.date.strftime("%d/%m/%y"))
                data.append(float(r.resting_heart_rate))

        data_graphs.append({
            'id': graphs[i], 
            'labels': labels, 
            'label': label[i],
            'backgroundColor': bg_colors[i],
            'borderColor': border_colors[i],
            'data': data,
            'text': texts[i],
        })

    return render(request, 'main/profile.html', {'data_graphs': data_graphs})


def weather(request):
    # API SINAICA
    url_sinaica = 'https://pacific-garden-86188.herokuapp.com/estacion'
    date = time.strftime("%Y-%m-%d", time.localtime())
    param = 'CO'
    range = 4
    station = 144
    contador = 0

    while True:
        try:
            if contador <= 1:
                payload = {'estacion': station, 'Fecha': date, 'parametro': param, 'rango': range}
                response_sinaica = requests.get(url_sinaica, params=payload)
                response_sinaica = json.loads(response_sinaica.text).pop()
            else:
                raise StopIteration
        except StopIteration:
            pollution = 'Por el momento no pudimos obtener estos datos.'
            break
        except:
            date = datetime.date.today() - datetime.timedelta(days=1)
            date = date.isoformat()
            contador += 1
        else:
            pollution = 'No realizar actividad física' if float(response_sinaica['valor']) > 1\
                                                else 'Clima apto para la actividad física'

    #API OPENWEATHER
    url_weather = 'http://api.openweathermap.org/data/2.5/weather'
    id = 3527646
    app_id = os.getenv('WEATHER_KEY', '')
    payload = {'id': id, 'appid': app_id}
    response_weather = requests.get(url_weather, params=payload)
    response_weather = json.loads(response_weather.text)
    temp = round(response_weather['main']['temp'] - 273.15) # Convert kelvin to celsius
    temp_min = round(response_weather['main']['temp_min'] - 273.15) # Convert kelvin to celsius
    temp_max = round(response_weather['main']['temp_max'] - 273.15) # Convert kelvin to celsius
    humidity = response_weather['main']['humidity']
    weather = {'temp': temp, 'temp_min': temp_min, 'temp_max': temp_max, 'humidity': humidity}

    context = {
        'pollution': pollution,
        'weather': weather,
    }

    return render(request, 'main/weather.html', context)


# def nutrition(request):
#     food_group = {
#         'A': {
#             'name': 'Alimentos de origen animal',
#             'energy': 40,  # kcal
#             'carbohydrates': 0,  # grames
#             'fat': 1,  # grames
#             'protein': 7,  # grames
#         },
#         'Az': {
#             'name': 'Azúcares',
#             'energy': 40,  # kcal
#             'carbohydrates': 10,  # grames
#             'fat': 0,  # grames
#             'protein': 0,  # grames
#         },
#         'CT': {
#             'name': 'Cereales y Tubérculos',
#             'energy': 70, # kcal
#             'carbohydrates': 15, # grames
#             'fat': 0, # grames
#             'protein': 2, # grames
#         },
#         'F': {
#             'name': 'Frutas',
#             'energy': 60,  # kcal
#             'carbohydrates': 15,  # grames
#             'fat': 0,  # grames
#             'protein': 0,  # grames
#         },
#         'G': {
#             'name': 'Grasas',
#             'energy': 70,  # kcal
#             'carbohydrates': 3,  # grames
#             'fat': 5,  # grames
#             'protein': 3,  # grames
#         },
#         'L': {
#             'name': 'Leguminosas',
#             'energy': 120,  # kcal
#             'carbohydrates': 20,  # grames
#             'fat': 1,  # grames
#             'protein': 8,  # grames
#         },
#         'LE': {
#             'name': 'Alimentos libres de energía',
#             'energy': 70,  # kcal
#             'carbohydrates': 15,  # grames
#             'fat': 0,  # grames
#             'protein': 2,  # grames
#         },
#         'LS': {
#             'name': 'Leche y Sustitutos',
#             'energy': 150,  # kcal
#             'carbohydrates': 12,  # grames
#             'fat': 8,  # grames
#             'protein': 9,  # grames
#         },
#         'V': {
#             'name': 'Vegetales',
#             'energy': 25,  # kcal
#             'carbohydrates': 4,  # grames
#             'fat': 0,  # grames
#             'protein': 2,  # grames
#         },
#     }
#     weight = {
#         'normal': {'f': (1600, 1800), 'm': (1800, 2000)},
#         'overweight': {'f': (1200, 1400), 'm': (1400, 1600)},
#     }
#     diets = {
#         # n kcal: {food group: portion}
#         1000: {'CT': 1, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
#         1200: {'CT': 2, 'V': 1, 'F': 1, 'LE': 1, 'G': 1},
#         1400: {'CT': 2, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
#         1600: {'CT': 2, 'V': 2, 'F': 1, 'LS': 1, 'G': 1},
#         1800: {'CT': 3, 'V': 1, 'F': 2, 'A': 1, 'LS': 1, 'G': 1},
#         2000: {'CT': 3, 'V': 1, 'F': 2, 'A': 2, 'LS': 1, 'G': 1},
#     }

#     height = 1.7
#     weight = 70
#     imc = weight / height**2
#     print(imc)

#     if imc < 18.5:
#         status = 'Desnutrición'
#     elif imc < 25:
#         status = 'Normal'
#     elif imc < 30:
#         status = 'Sobrepeso'
#     else:
#         status = 'Obesidad'

#     return HttpResponse(status)
