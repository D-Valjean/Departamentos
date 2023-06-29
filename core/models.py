from django.db import models

# Create your models here.


class Ticket(models.Model):
    Descripcion_del_Problema = models.TextField(blank=True)
    Departamento = models.CharField(max_length=200)
    Estado = models.BooleanField(default=False)
    Fecha = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.Descripcion_del_Problema + ' del ' + str(self.Fecha)