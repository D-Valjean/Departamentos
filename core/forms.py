from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket



class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__' no usar __all__ porque trae todos los permisos de super user
        fields = ['username','password1','password2']



class CustomTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['Descripcion_del_Problema','Departamento']
        widgets = {
            'Departamento':forms.HiddenInput()
        }