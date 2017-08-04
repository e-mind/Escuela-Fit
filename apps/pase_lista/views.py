# from django.shortcuts import render, redirect
from django.http import JsonResponse

def json_chart(request):
    json_data = {
        'labels': ["January", "February", "March", "April", "May", "June", "July"],
        'datasets': [{
            'label': "My First dataset",
            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
            'borderColor': 'rgb(255, 99, 132)',
            'data': [0, 10, 5, 2, 20, 30, 45],
        }]
    }
    return JsonResponse(json_data)
