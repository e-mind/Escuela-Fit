from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView

from apps.physical_record.models import PhysicalRecord
from .models import *


@login_required
def list(request):
    student = request.user.student
    diets = []
    for schedule in ['breakfast', 'collation1', 'meal', 'collation2', 'dinner']:
        try:
            diets.append(student.nutrition_set.filter(schedule=schedule)[0])
        except:
            continue

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
    total_calories = 0
    for nf in nutrition_food:
        if nf.food_table == 'aoa_alto':
            food = AOAAltoEnGrasa.objects.get(pk=nf.food_id)
            diet.append(('Alimentos de Origen Animal Altos en Grasa', food, nf))
        elif nf.food_table == 'aoa_bajo':
            food = AOABajosEnGrasa.objects.get(pk=nf.food_id)
            diet.append(('Alimentos de Origen Animal Bajos en Grasa', food, nf))
        elif nf.food_table == 'aoa_moderado':
            food = AOAModeradosEnGrasa.objects.get(pk=nf.food_id)
            diet.append(('Alimentos de Origen Animal Moderados en Grasa', food, nf))
        elif nf.food_table == 'aoa_muy_bajo':
            food = AOAMuyBajosEnGrasa.objects.get(pk=nf.food_id)
            diet.append(('Alimentos de Origen Animal Muy Bajos en Grasa', food, nf))
        elif nf.food_table == 'cereal_grasa':
            food = Cerealescongrasa.objects.get(pk=nf.food_id)
            diet.append(('Cereal con Grasa', food, nf))
        elif nf.food_table == 'cereal':
            food = Cerealessingrasa.objects.get(pk=nf.food_id)
            diet.append(('Cereal sin grasa', food, nf))
        elif nf.food_table == 'frutas':
            food = Frutas.objects.get(pk=nf.food_id)
            diet.append(('Frutas', food, nf))
        elif nf.food_table == 'leguminosas':
            food = Leguminosas.objects.get(pk=nf.food_id)
            diet.append(('Leguminosas', food, nf))
        elif nf.food_table == 'verduras':
            food = Verduras.objects.get(pk=nf.food_id)
            diet.append(('Verduras', food, nf))

    for type, food, nf in diet:
        total_calories += int(food.energiakcal)

    if nutrition.schedule == 'breakfast':
        title = 'Desayuno'
    elif nutrition.schedule == 'collation1':
        title = 'Colación 1'
    elif nutrition.schedule == 'meal':
        title = 'Comida'
    elif nutrition.schedule == 'collation2':
        title = 'Colación 2'
    else:
        title = 'Cena'

    context = {
        'nutrition': nutrition,
        'diet': diet,
        'title': title,
        'total_calories': total_calories,
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
                'breakfast': {
                    1000: {'C': 1, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
                    1200: {'C': 2, 'V': 1, 'F': 1, 'LE': 1, 'G': 1},
                    1400: {'C': 2, 'V': 1, 'F': 1, 'A': 1, 'LS': 1, 'G': 1},
                    1600: {'C': 2, 'V': 2, 'F': 1, 'LS': 1, 'G': 1},
                    1800: {'C': 3, 'V': 1, 'F': 2, 'A': 1, 'LS': 1, 'G': 1},
                    2000: {'C': 3, 'V': 1, 'F': 2, 'A': 2, 'LS': 1, 'G': 1},
                },
                'collation1': {
                    1000: {},
                    1200: {'F': 1, 'LS': 1},
                    1400: {'F': 1, 'LS': 1},
                    1600: {'V': 1, 'A': 1},
                    1800: {'C': 1, 'A': 1},
                    2000: {'C': 2, 'V': 2},
                },
                'meal': {
                    1000: {'C': 2, 'V': 2, 'F': 1, 'A': 1, 'G': 1, 'LS': 1},
                    1200: {'C': 2, 'V': 2, 'F': 1, 'A': 2, 'G': 1, 'LS': 1},
                    1400: {'C': 2, 'V': 2, 'LE': 1, 'A': 2, 'G': 1},
                    1600: {'C': 2, 'V': 2, 'F': 1, 'A': 2, 'G': 1, 'LS': 1},
                    1800: {'C': 2, 'V': 2, 'F': 1, 'A': 2, 'G': 1, 'LS': 1},
                    2000: {'C': 3, 'V': 2, 'F': 1, 'A': 2, 'LE': 1, 'G': 1, 'LS': 1},
                },
                'collation2': {
                    1000: {'LS': 1},
                    1200: {'V': 1, 'LS': 1},
                    1400: {'C': 1, 'LS': 1},
                    1600: {'C': 2, 'F': 1},
                    1800: {'C': 1, 'LS': 1},
                    2000: {'C': 2, 'F': 1},
                },
                'dinner': {
                    1000: {'C': 1, 'V': 1, 'F': 1, 'LE': 1},
                    1200: {'C': 1, 'V': 1, 'LS': 1},
                    1400: {'C': 1, 'V': 1, 'F': 1, 'A': 1, 'LS': 1},
                    1600: {'C': 1, 'V': 2, 'F': 1, 'A': 1, 'LE': 1},
                    1800: {'C': 1, 'V': 2, 'F': 1, 'A': 1, 'LE': 1},
                    2000: {'C': 1, 'V': 2, 'F': 1, 'A': 1, 'LS': 1},
                },
            }

            record = PhysicalRecord.objects.filter(student=request.user.student)

            if not record:
                url = reverse_lazy('record:create', args=(request.user.student.pk,)) + "?next=nutrition"
                return redirect(url)
            else:
                # BMR Men = (10 x weight(kg)) + (6,25 × height(cm)) – (5 × age(years)) + 5
                # BMR Women = (10 x weight(kg)) + (6,25 × height(cm)) – (5 × age(years)) – 161
                r = record[0]

                if r.student.gender == 'H':
                    bmr = (10 * r.weight) + (6.25 * (r.height*100)) - (5 * r.student.age) + 5
                else:
                    bmr = (10 * r.weight) + (6.25 * (r.height*100)) - (5 * r.student.age) - 161

            if bmr <= 1100: calories = 1000
            elif bmr <= 1300: calories = 1200
            elif bmr <= 1500: calories = 1400
            elif bmr <= 1700: calories = 1600
            elif bmr <= 1900: calories = 1800
            else: calories = 2000
            request.session['diet'] = diets[schedule][calories]
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

            for key in ['diet', 'schedule', 'aoa_alto', 'aoa_moderado', 'aoa_bajo', 'aoa_muy_bajo', 'cereal', 'cereal_grasa', 'frutas', 'leguminosas', 'verduras']:
                try:
                    del request.session[key]
                except:
                    continue
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
        record = PhysicalRecord.objects.filter(student=request.user.student)

        if not record:
            url = reverse_lazy('record:create', args=(request.user.student.pk,)) + "?next=nutrition"
            return redirect(url)
        else:
            # BMR Men = (10 x weight(kg)) + (6,25 × height(cm)) – (5 × age(years)) + 5
            # BMR Women = (10 x weight(kg)) + (6,25 × height(cm)) – (5 × age(years)) – 161
            r = record[0]

            if r.student.gender == 'H':
                bmr = (10 * r.weight) + (6.25 * (r.height*100)) - (5 * r.student.age) + 5
            else:
                bmr = (10 * r.weight) + (6.25 * (r.height*100)) - (5 * r.student.age) - 161

            return render(request, 'nutrition/create.html', {'bmr': bmr})


@login_required
def update_food(request, key, nf_pk):
    if request.method == 'POST':
        for key, value in request.POST.items():
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

                nf = Nutrition_Food.objects.get(pk=nf_pk)
                nf.food_id = food.pk
                nf.save()

                return redirect(referer)

    if key == 'aoa_alto':
        title = 'Alimentos de Origen Animal Altos en Grasa'
        food = AOAAltoEnGrasa.objects.all()
    elif key == 'aoa_bajo':
        title = 'Alimentos de Origen Animal Bajos en Grasa'
        food = AOABajosEnGrasa.objects.all()
    elif key == 'aoa_moderado':
        title = 'Alimentos de Origen Animal Moderados en Grasa'
        food = AOAModeradosEnGrasa.objects.all()
    elif key == 'aoa_muy_bajo':
        title = 'Alimentos de Origen Animal Muy Bajos en Grasa'
        food = AOAMuyBajosEnGrasa.objects.all()
    elif key == 'cereal_grasa':
        title = 'Cereales con Grasa'
        food = Cerealescongrasa.objects.all()
    elif key == 'cereal':
        title = 'Cereales sin Grasa'
        food = Cerealessingrasa.objects.all()
    elif key == 'frutas':
        title = 'Frutas'
        food = Frutas.objects.all()
    elif key == 'leguminosas':
        title = 'Leguminosas'
        food = Leguminosas.objects.all()
    elif key == 'verduras':
        title = 'Verduras'
        food = Verduras.objects.all()

    referer = request.META.get('HTTP_REFERER', '')

    letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    context = {
        'letters': letters,
        'food': food,
        'title': title,
        'key': key,
        'quantity': 1,
        'referer': referer,
    }

    return render(request, 'nutrition/update.html', context)

class NutritionDelete(DeleteView):
    model = Nutrition
    template_name = "nutrition/delete.html"
    success_url = reverse_lazy('nutrition:list')
