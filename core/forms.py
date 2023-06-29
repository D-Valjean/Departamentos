from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ticket



class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__' no usar __all__ porque trae todos los permisos de super user
        fields = ['username','first_name','last_name','email','password1','password2']



class CustomTicket(forms.Form):
    Descripcion_del_Problema = forms.CharField(widget=forms.Textarea)
    Departamento = forms.CharField(disabled=True)
    # Estado = forms.BooleanField(disabled=True)