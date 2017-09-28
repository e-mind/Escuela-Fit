from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import attendance
from apps.students.models import Student


def index(request, student=None):
    attendances = Attendance.objects.filter(student=student).count()
    data_response = {
        # 'labels': [str(attendances)],
        # 'datasets': [
        #     {
        #         'label': 'attendance',
        #         'backgoundColor': 'rgb(255,0,0)',
        #         'borderColor': 'rgb(255,0,0)',
        #         'data': [attendances],
        #     }
        # ],
        'labels': ['Enero', 'Febrero', 'Marzo'],
        'datasets': [
            {
                'label': 'asistencia',
                'backgroundColor': 'rgba(255,0,0,0.3)',
                'borderColor': 'rgba(255,0,0,0.5)',
                'data': [3, 5, 4],
            }
        ],
    }

    context = {
        'data_response': data_response,
    }
    
    return render(request, 'attendance/index.html', context)


@csrf_exempt
def register(request):
    rfid = request.POST['rfid']
    student = Student.objects.get(card_code=rfid)
    registro = student.attendance_set.create()
    return HttpResponse(rfid)
