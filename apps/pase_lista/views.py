from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Asistencia
from apps.alumnos.models import AlumnoDatosPersonales


def asistencia(request, alumno=None):
    asistencias = Asistencia.objects.filter(alumno=alumno).count()
    data_response = {
        # 'labels': [str(asistencias)],
        # 'datasets': [
        #     {
        #         'label': 'Asistencia',
        #         'backgoundColor': 'rgb(255,0,0)',
        #         'borderColor': 'rgb(255,0,0)',
        #         'data': [asistencias],
        #     }
        # ],
        'labels': ['Enero', 'Febrero', 'Marzo'],
        'datasets': [
            {
                'label': 'Asistencia',
                'backgroundColor': 'rgba(255,0,0,0.3)',
                'borderColor': 'rgba(255,0,0,0.5)',
                'data': [3, 5, 4],
            }
        ],
    }
    context = {
        'data_response': data_response,
    }
    return render(request, 'pase_lista/asistencia.html', context)

@csrf_exempt
def registro(request):
    rfid = request.POST['rfid']
    alumno = AlumnoDatosPersonales.objects.get(codigo_tarjeta=rfid)
    registro = alumno.asistencia_set.create()
    return HttpResponse(rfid)
