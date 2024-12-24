from django.contrib import admin
from .models import Ranande, ServiceKhak

# admin.site.register(Ranande)


@admin.register(Ranande)
class RanandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mobile')


@admin.register(ServiceKhak)
class ServiceKhakAdmin(admin.ModelAdmin):
    list_display = ('id', 'ranande', 'mohandes')
