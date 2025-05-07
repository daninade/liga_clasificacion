from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Equipo
def index(request):
    template = loader.get_template('my_first_html.html')
    return HttpResponse(template.render())
    #return HttpResponse("Hello, world. You're at the clasification index.")

def home(request):
    return HttpResponse("Hello, this is home")

def clasificacion(request):
    myteams = Equipo.objects.all().values()
    template = loader.get_template('all_teams.html')
    context = {
        "teams" : myteams,
    }
    return HttpResponse(template.render(context, request))