# from django.shortcuts import render, redirect
from django.http import JsonResponse

def json_data(request):
    data_response = [5, 10, 20, 30, 20, 10, 5]
    return JsonResponse(data_response, safe=False)
