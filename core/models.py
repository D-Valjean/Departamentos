from django.db import models

# Create your models here.


class Ticket(models.Model):
    Descripcion_del_Problema = models.TextField(blank=True, verbose_name='Descripcion del Problema')
    Departamento = models.CharField(max_length=200,verbose_name='Departamento')
    Estado = models.BooleanField(default=False,verbose_name='Estado')
    Fecha = models.DateField(auto_now_add=True,verbose_name='Fecha de envio')

    def __str__(self) -> str:
        return self.Descripcion_del_Problema + ' del ' + str(self.Fecha)