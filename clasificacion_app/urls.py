from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("home", views.home, name="home"),
    path('clasificacion',views.clasificacion, name='clasificacion'),
    path('calendario', views.calendario, name='calendario'),
    path('jornada', views.jornada, name='jornada')
]