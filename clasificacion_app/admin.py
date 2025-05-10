from django.contrib import admin
from .models import *
from django.apps import apps
# Register your models here.

app_models = apps.get_app_config('clasificacion_app').get_models()
for model in app_models:
    admin.site.register(model)