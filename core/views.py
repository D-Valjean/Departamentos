from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomCreationForm, CustomTicket
from django.contrib.auth import authenticate, login
from . import models
from .models import Ticket
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    return render(request,'cores/home.html')



@login_required
def products(request):
    return render(request,'cores/products.html')


def exit(request):
    logout(request)
    return redirect('home')

@login_required
def listcompleted(request):
    t = models.Ticket.objects.filter(Estado=True)

    return render(request,'cores/completados.html',{
        't':t
    })

@login_required
def listticket(request):
    t = models.Ticket.objects.filter(Estado=False)
    if request.method =='POST':
        if 'cambiar_Estado' in request.POST:
            obj_id = request.POST['obj_id']
            obj = models.Ticket.objects.get(id=obj_id)
            obj.Estado = True
            obj.save()
        elif 'elimnar_ticket' in request.POST:
            obj_id = request.POST['obj_id']
            models.Ticket.objects.filter(id=obj_id).delete()
        
        return redirect('pendiente') 

    title ='Tickets'
    return render(request,'cores/pendientes.html',{
        'data' : t,
        'p':title 
    })


# def cambiar_Estado(request,ticket_id):
#     obj = models.Ticket.objects.get(pk=ticket_id)
#     obj.Estado = True
#     obj.save()
#     return redirect('pendiente')


# def eleminar_ticket(request,ticket_id):
#     obj = models.Ticket.objects.get(pk=ticket_id)
#     obj.delete()

#     return redirect('pendiente')




def register(request):
    data = {
        'form': CustomCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username= user_creation_form.cleaned_data['username'], password= user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')

    if request.user.is_superuser: 
        return render(request,'registration/register.html',data)

@login_required
def TicketView(request):
    data = CustomTicket(initial={'Departamento': request.user.username})
    def enviar_correo():
       subject = request.user.username
       message = request.POST['Descripcion_del_Problema']
       email_from = settings.EMAIL_HOST_USER
       recipient_list = [''] #direccion de correo de destino
       send_mail(subject, message, email_from, recipient_list)
    if request.method=="POST":
        data = CustomTicket(data=request.POST)
        if data.is_valid():
            data.save()
            enviar_correo()
            return redirect('home')

    return render(request,'registration/ticket.html',{'form':data})


    # data:dict = {
    #     'form': CustomTicket(initial={'Departamento': request.user.username})
    # }
    
    # if request.method == 'POST':
    #     User_ticket = CustomTicket(data=request.POST)
    #     if User_ticket.is_valid():
    #         ticket = User_ticket.save(commit=True)
    #         ticket.save()
    #         Ticket.objects.create(
    #             descripcion_del_problema=request.POST['descripcion_delproblema'],departamento=request.POST['departamento'])
    #         # models.Ticket.objects.create(Descripcion_del_Problema=User_ticket.cleaned_data['Descripcion_del_Problema'],Departamento=User_ticket.cleaned_data['Departamento'])
    #         return redirect('home')
        
        
    # return render(request,'registration/ticket.html',data)





    # if request.method == 'POST':
    #     form = CustomTicket(request.POST)
    #     if form.is_valid():
    #         descripcion = form.cleaned_data['Descripcion_del_Problema']
    #         departamento = form.cleaned_data['Departamento']
    #         Ticket.objects.create(Departamento=request.POST[departamento],Descripcion_del_Problema=request.POST[descripcion],Estado=False)
    #         return redirect('home')
    # else:
    #     # Inicializar el formulario con el nombre de usuario del usuario actual
    #     form = CustomTicket(initial={'Departamento': request.user.username})
    # return render(request, 'registration/ticket.html', {'form': form})





    # user = authenticate(username = )
    # if request.method == 'GET':
    #     return render(request, 'registration/ticket.html', {
    #         'form': CustomTicket()
    #     })
    # else:
    #     Ticket.objects.create(
    #         Departamento=request.POST[username], Descripcion_del_Problema=request.POST['Descripcion_del_Problema'])
    #     return redirect('home')
        
