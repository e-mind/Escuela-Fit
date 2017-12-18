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

    try:
        payload = {'estacion': station, 'Fecha': date, 'parametro': param, 'rango': range}
        response_sinaica = requests.get(url_sinaica, params=payload)
        response_sinaica = json.loads(response_sinaica.text).pop()
    except:
        pollution = 'Por el momento no pudimos obtener estos datos.'
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
