from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import *


@login_required
def list(request):
    student = request.user.student
    diets = student.nutrition_set.all()

    context = {
        'diets': diets,
    }

    return render(request, 'nutrition/list.html', context)


@login_required
def cancel(request):
    for key in ['diet', 'schedule', 'aoa_alto', 'aoa_moderado', 'aoa_bajo', 'aoa_muy_bajo', 'cereal', 'cereal_grasa', 'frutas', 'leguminosas', 'verduras']:
        try:
            del request.session[key]
        except:
            continue
    return redirect(reverse_lazy('nutrition:create'))


@login_required
def detail(request, schedule, pk):
    nutrition = Nutrition.objects.get(pk=pk)
    nutrition_food = nutrition.nutrition_food_set.all()
    diet = []
    for n in nutrition_food:
        if n.food_table == 'aoa_alto':
            food = AOAAltoEnGrasa.objects.get(pk=n.food_id)
            diet.append(('Alimentos de Origen Animal Altos en Grasa', food.alimentos))
        elif n.food_table == 'aoa_bajo':
            food = AOABajosEnGrasa.objects.get(pk=n.food_id)
            diet.append(('Alimentos de Origen Animal Bajos en Grasa', food.alimentos))
        elif n.food_table == 'aoa_moderado':
            food = AOAModeradosEnGrasa.objects.get(pk=n.food_id)
            diet.append(('Alimentos de Origen Animal Moderados en Grasa', food.alimentos))
        elif n.food_table == 'aoa_muy_bajo':
            food = AOAMuyBajosEnGrasa.objects.get(pk=n.food_id)
            diet.append(('Alimentos de Origen Animal Muy Bajos en Grasa', food.alimentos))
        elif n.food_table == 'cereal_grasa':
            food = Cerealescongrasa.objects.get(pk=n.food_id)
            diet.append(('Cereal con Grasa', food.alimentos))
        elif n.food_table == 'cereal':
            food = Cerealessingrasa.objects.get(pk=n.food_id)
            diet.append(('Cereal sin grasa', food.alimentos))
        elif n.food_table == 'frutas':
            food = Frutas.objects.get(pk=n.food_id)
            diet.append(('Frutas', food.alimentos))
        elif n.food_table == 'leguminosas':
            food = Leguminosas.objects.get(pk=n.food_id)
            diet.append(('Leguminosas', food.alimentos))
        elif n.food_table == 'verduras':
            food = Verduras.objects.get(pk=n.food_id)
            diet.append(('Verduras', food.alimentos))

    if nutrition.schedule == 'breakfast':
        title = 'Desayuno'
    elif nutrition.schedule == 'collation1':
        title = 'Colación 1'
    elif nutrition.schedule == 'meal':
        title = 'COmida'
    elif nutrition.schedule == 'collation2':
        title = 'Colación 2'
    else:
        title = 'Cena'

    context = {
        'nutrition': nutrition,
        'diet': diet,
        'title': title,
    }

    return render(request, 'nutrition/detail.html', context)
    

@login_required
def create(request, schedule=''):
    if schedule and schedule in ['breakfast', 'collation1', 'meal', 'collation2', 'dinner']:
        if request.method == 'POST':
            for key, value in request.POST.items():
                if key not in ['csrfmiddlewaretoken']:
                    request.session[key] = value
        
        if 'diet' not in request.session:
            diets = {
                # n kcal: {food group: portion}
                1000: {'C': 1, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
                1200: {'C': 2, 'V': 1, 'F': 1, 'LE': 1, 'G': 1},
                1400: {'C': 2, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
                1600: {'C': 2, 'V': 2, 'F': 1, 'LS': 1, 'G': 1},
                1800: {'C': 3, 'V': 1, 'F': 2, 'A': 1, 'LS': 1, 'G': 1},
                2000: {'C': 3, 'V': 1, 'F': 2, 'A': 2, 'LS': 1, 'G': 1},
            }
            calories = 1000
            request.session['diet'] = diets[calories]
            request.session['schedule'] = schedule

        if 'A' in request.session['diet'] and 'aoa_alto' not in request.session:
            title = 'Alimentos de Origen Animal Altos en Grasa'
            key = 'aoa_alto'
            food = AOAAltoEnGrasa.objects.all()
            quantity = request.session['diet']['A']
        elif 'AB' in request.session['diet'] and 'aoa_bajo' not in request.session:
            title = 'Alimentos de Origen Animal Bajos en Grasa'
            key = 'aoa_bajo'
            food = AOABajosEnGrasa.objects.all()
        elif 'AM' in request.session['diet'] and 'aoa_moderado' not in request.session:
            title = 'Alimentos de Origen Animal Moderados en Grasa'
            key = 'aoa_moderado'
            food = AOAModeradosEnGrasa.objects.all()
        elif 'AMB' in request.session['diet'] and 'aoa_muy_bajo' not in request.session:
            title = 'Alimentos de Origen Animal Muy Bajos en Grasa'
            key = 'aoa_muy_bajo'
            food = AOAMuyBajosEnGrasa.objects.all()
        elif 'C' in request.session['diet'] and 'cereal_grasa' not in request.session:
            title = 'Cereales con Grasa'
            key = 'cereal_grasa'
            food = Cerealescongrasa.objects.all()
            quantity = request.session['diet']['C']
        elif 'CS' in request.session['diet'] and 'cereal' not in request.session:
            title = 'Cereales sin Grasa'
            key = 'cereal'
            food = Cerealessingrasa.objects.all()
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
            nutrition = Nutrition.objects.create(student=request.user.student, schedule=request.session['schedule'])
            for key, value in request.session.items():
                if key in ['aoa_alto', 'aoa_moderado', 'aoa_bajo', 'aoa_muy_bajo', 'cereal', 'cereal_grasa', 'frutas', 'leguminosas', 'verduras']:
                    if key == 'aoa_alto':
                        food = AOAAltoEnGrasa.objects.get(alimentos=value)
                    elif key == 'aoa_bajo':
                        food = AOABajosEnGrasa.objects.get(alimentos=value)
                    elif key == 'aoa_moderado':
                        food = AOAModeradosEnGrasa.objects.get(alimentos=value)
                    elif key == 'aoa_muy_bajo':
                        food = AOAMuyBajosEnGrasa.objects.get(alimentos=value)
                    elif key == 'cereal_grasa':
                        food = Cerealescongrasa.objects.get(alimentos=value)
                    elif key == 'cereal':
                        food = Cerealessingrasa.objects.get(alimentos=value)
                    elif key == 'frutas':
                        food = Frutas.objects.get(alimentos=value)
                    elif key == 'leguminosas':
                        food = Leguminosas.objects.get(alimentos=value)
                    elif key == 'verduras':
                        food = Verduras.objects.get(alimentos=value)

                    Nutrition_Food.objects.create(nutrition=nutrition, food_id=food.id, food_table=key)

            print(request.session.items())
            request.session.flush()
            return redirect(reverse_lazy('nutrition:detail', args=(nutrition.schedule, nutrition.pk)))

        letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
        context = {
            'letters': letters,
            'food': food,
            'title': title,
            'key': key,
            'quantity': quantity,
            'schedule': schedule,
        }

        return render(request, 'nutrition/create.html', context)  

    elif 'schedule' in request.session:
        return redirect(reverse_lazy('nutrition:create', args=(request.session['schedule'],)))
    else:        
        return render(request, 'nutrition/create.html', {})
