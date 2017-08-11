# from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


def json_data(request):
    data_response = [5, 10, 20, 30, 20, 10, 5]
    return JsonResponse(data_response, safe=False)

@csrf_exempt
def asistencia(request):
    rfid = request.POST['rfid']
    print(rfid)
    return HttpResponse(rfid)
