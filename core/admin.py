from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Ticket)
class ATicket(admin.ModelAdmin):
    list_display = ('id','Descripcion_del_Problema','Departamento','Estado')