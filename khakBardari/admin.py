from django.contrib import admin
from .models import Ranande


@admin.register(Ranande)
class RanandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mobile')
