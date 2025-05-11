from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Equipo, Partido, Jornada, Liga

def index(request):
    ligas = Liga.objects.all()
    template = loader.get_template('pagina_principal.html')
    context ={
        "leagues" : ligas
    }
    return HttpResponse(template.render(context, request))

def home(request):
    return HttpResponse("Hello, this is home")

def clasificacion(request, liga_id):
    liga = get_object_or_404(Liga, id=liga_id)
    template = loader.get_template('clasificacion.html')
    context = {
        "liga" : liga,
    }
    return HttpResponse(template.render(context, request))

def jornada(request, liga_id):
    liga = get_object_or_404(Liga, id=liga_id)
    #jornada = get_object_or_404(Jornada, liga=liga, numero=1)
    partidos = Partido.objects.filter(jornada=1)
    template = loader.get_template('jornada.html')

    context = {
        "partido" : partidos,
        "jornada" : jornada
    }
    return HttpResponse(template.render(context, request))

def calendario(request, liga_id):
    return HttpResponse("Calendario temporada")

def ligas(request):
    template = loader.get_template('liga.html')

    return HttpResponse(template.render(request))

def menu_opciones(request, liga_id):
    liga = get_object_or_404(Liga, id=liga_id)
    jornada = get_object_or_404(Jornada, numero=1)
    return render(request, 'menu_opciones.html', {'liga': liga, 'jornada' : jornada})