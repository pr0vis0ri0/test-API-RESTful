from django.shortcuts import render
import requests

# Create your views here.

# def lista_departamentos(request):
#     response = requests.get('http://localhost:8000/restful/comuna/')
#     data = response.json()
#     for d in data :
#         global id_region;
#         id_region = d.get('id_region')
#         response2 = requests.get(f'http://localhost:8000/restful/region/{id_region}')
#         data2 = response2.json()    
#         return render(request, 'departamentos.html', {'data' : data, 'data2' : data2})

# def lista_departamentos(request):
#     response = requests.get('http://localhost:8000/restful/comuna/')
#     data = response.json()
#     response2 = requests.get('http://localhost:8000/restful/region/')
#     data2 = response2.json()    
#     return render(request, 'departamentos.html', {'data' : data, 'data2' : data2})

def lista_departamentos(request):
    response = requests.get('http://localhost:8000/restful/region/13')
    data = response.json()
    response2 = requests.get('http://localhost:8000/restful/comuna/')
    data2 = response2.json()    
    return render(request, 'departamentos.html', {'data' : data, 'data2' : data2})