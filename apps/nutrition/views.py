from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                request.session[key] = value
    
    # if 'diet' not in request.session:
    diets = {
        # n kcal: {food group: portion}
        1000: {'CT': 1, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
        1200: {'CT': 2, 'V': 1, 'F': 1, 'LE': 1, 'G': 1},
        1400: {'CT': 2, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
        1600: {'CT': 2, 'V': 2, 'F': 1, 'LS': 1, 'G': 1},
        1800: {'CT': 3, 'V': 1, 'F': 2, 'A': 1, 'LS': 1, 'G': 1},
        2000: {'CT': 3, 'V': 1, 'F': 2, 'A': 2, 'LS': 1, 'G': 1},
    }
    calories = 1000
    request.session['diet'] = diets[calories]

    if 'A' in request.session['diet'] and 'aoa_alto' not in request.session:
        title = 'Alimentos de Origen Animal Altos en Grasa'
        key = 'aoa_alto'
        food = AOAAltoEnGrasa.objects.all()
        quantity = request.session['diet']['A']
    # elif 'aoa_bajo' not in request.session:
    #     title = 'Alimentos de Origen Animal Bajos en Grasa'
    #     key = 'aoa_bajo'
    #     food = AOABajosEnGrasa.objects.all()
    # elif 'aoa_moderado' not in request.session:
    #     title = 'Alimentos de Origen Animal Moderados en Grasa'
    #     key = 'aoa_moderado'
    #     food = AOAModeradosEnGrasa.objects.all()
    # elif 'aoa_muy_bajo' not in request.session:
    #     title = 'Alimentos de Origen Animal Muy Bajos en Grasa'
    #     key = 'aoa_muy_bajo'
    #     food = AOAMuyBajosEnGrasa.objects.all()
    elif 'CT' in request.session['diet'] and 'cereal_grasa' not in request.session:
        title = 'Cereales con Grasa'
        key = 'cereal_grasa'
        food = Cerealescongrasa.objects.all()
        quantity = request.session['diet']['CT']
    # elif 'cereal' not in request.session:
    #     title = 'Cereales sin Grasa'
    #     key = 'cereal'
    #     food = Cerealessingrasa.objects.all()
    elif 'F' in request.session['diet'] and 'frutas' not in request.session:
        title = 'Frutas'
        key = 'frutas'
        food = Frutas.objects.all()
        quantity = request.session['diet']['F']
    elif 'L' in request.session['diet'] and 'leguminosas' not in request.session:
        title = 'Leguminosas'
        key = 'leguminosas'
        food = Leguminosas.objects.all()
        quantity = request.session['diet']['L']
    elif 'V' in request.session['diet'] and 'verduras' not in request.session:
        title = 'Verduras'
        key = 'verduras'
        food = Verduras.objects.all()
        quantity = request.session['diet']['V']
    else:
        items = request.session.items()
        request.session.flush()
        return HttpResponse(items)

    letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    context = {
        'food': food,
        'letters': letters,
        'title': title,
        'key': key,
        'quantity': quantity,
    }

    return render(request, 'nutrition/index.html', context)

    # if 'aoa_alto' not in request.session:
    #     title = 'Alimentos de Origen Animal Altos en Grasa'
    #     key = 'aoa_alto'
    #     food = AOAAltoEnGrasa.objects.all()
    # elif 'aoa_bajo' not in request.session:
    #     title = 'Alimentos de Origen Animal Bajos en Grasa'
    #     key = 'aoa_bajo'
    #     food = AOABajosEnGrasa.objects.all()
    # elif 'aoa_moderado' not in request.session:
    #     title = 'Alimentos de Origen Animal Moderados en Grasa'
    #     key = 'aoa_moderado'
    #     food = AOAModeradosEnGrasa.objects.all()
    # elif 'aoa_muy_bajo' not in request.session:
    #     title = 'Alimentos de Origen Animal Muy Bajos en Grasa'
    #     key = 'aoa_muy_bajo'
    #     food = AOAMuyBajosEnGrasa.objects.all()
    # elif 'cereal_grasa' not in request.session:
    #     title = 'Cereales con Grasa'
    #     key = 'cereal_grasa'
    #     food = Cerealescongrasa.objects.all()
    # elif 'cereal' not in request.session:
    #     title = 'Cereales sin Grasa'
    #     key = 'cereal'
    #     food = Cerealessingrasa.objects.all()
    # elif 'frutas' not in request.session:
    #     title = 'Frutas'
    #     key = 'frutas'
    #     food = Frutas.objects.all()
    # elif 'leguminosas' not in request.session:
    #     title = 'Leguminosas'
    #     key = 'leguminosas'
    #     food = Leguminosas.objects.all()
    # elif 'verduras' not in request.session:
    #     title = 'Verduras'
    #     key = 'verduras'
    #     food = Verduras.objects.all()
    # else:
    #     items = request.session.items()
    #     request.session.flush()
    #     return HttpResponse(items)

    
