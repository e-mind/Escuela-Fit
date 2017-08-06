# from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

import serial

def json_data(request):
    data_response = [5, 10, 20, 30, 20, 10, 5]
    return JsonResponse(data_response, safe=False)

def asistencia(request):
    arduino = serial.Serial('COM4', 9600)
    rawString = str(arduino.readline())
    arduino.close()
    return JsonResponse(rawString, safe=False)