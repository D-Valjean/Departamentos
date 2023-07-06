from django.urls import path
from . import views



urlpatterns =[
    path('', views.home, name='home'),
    path('product/', views.products, name='products'),
    path('logout/',views.exit, name='exit'),
    path('register/',views.register, name="register"),
    path('ticket/',views.TicketView,name='ticket'),
    path('pendiente/',views.listticket,name='pendiente'),
    path('completados/',views.listcompleted,name='completados'),
    # path('pendiente/<int:ticket_id>/',views.cambiar_Estado,name='cambiar_estado'),
    # path('pendiente/<int:ticket_id>/',views.eleminar_ticket,name='eleminar_ticket'),
]