from django.shortcuts import render
import requests

# Create your views here.

def lista_departamentos(request):
    response = requests.get('http://localhost:8000/back/get/')
    data = response.json()
    return render(request, 'departamentos.html', {'data' : data})
