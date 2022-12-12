from django.urls import path
from .views import home,contacto,galeria,eliminar_portafolio ,\
    agregar_portafolio,listar_portafolio,modificar_portafolio,registro

urlpatterns = [
    path('',home,name="home"),
    path('contacto/',contacto,name="contacto"),
    path('galeria',galeria,name="galeria"),
    path('agregar-portafolio/',agregar_portafolio, name="agregar_portafolio"),
    path('listar-portafolio/',listar_portafolio, name="listar_portafolio"),
    path('modificar-portafolio/<id>/',modificar_portafolio, name="modificar_portafolio"),
    path('eliminar-portafolio/<id>/',eliminar_portafolio, name="eliminar_portafolio"),
    path('registro/',registro, name = "registro"),
]