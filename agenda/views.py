from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def consultas(request):
    return render(request, 'consultas.html')

def pacientes(request):
    return render(request, 'pacientes.html')

def medicos(request):
    return render(request, 'medicos.html')

def contato(request):
    return render(request, 'contato.html')

def agendar(request):
    return render(request, 'agendar.html')