# from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Asistencia
from apps.alumnos.models import AlumnoDatosPersonales


def json_data(request):
    data_response = [5, 10, 20, 30, 20, 10, 5]
    return JsonResponse(data_response, safe=False)

@csrf_exempt
def asistencia(request):
    rfid = request.POST['rfid']
    alumno = AlumnoDatosPersonales.objects.get(codigo_tarjeta=rfid)
    registro = alumno.asistencia_set.create()
    print(registro.id)
    print(registro.fecha)
    print(registro.hora)
    print(registro.alumno)
    return HttpResponse(rfid)
