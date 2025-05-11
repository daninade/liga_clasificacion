from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("home/", views.home, name="home"),
    path('liga/<int:liga_id>/', views.menu_opciones, name='opciones_liga'),
    path('liga/<int:liga_id>/clasificacion/',views.clasificacion, name='clasificacion'),
    path('liga/<int:liga_id>/calendario/', views.calendario, name='calendario'),
    path('liga/<int:liga_id>/jornada/', views.jornada, name='jornada'),
]