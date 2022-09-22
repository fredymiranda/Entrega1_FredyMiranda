from django.urls import path
from AppIntermedia.views import *

urlpatterns = [
    #Home
    path('', inicio, name="Inicio"),
    #Creacion
    path('Crear/Sucursales', crearSucursales, name='CrearSucursales'),
    path('Crear/Empleados', crearEmpleados, name='CrearEmpleados'),
    path('Crear/Servicios', crearServicios, name='CrearServicios'),
    #Consulta Sucursales
    path('Consulta/Sucursales/', consultarSucursales, name='ConsultarSucursales'),
    path('Consulta/Sucursales/Resultados/', resultadosSucursales),
    #Consulta Servicios
    path('Consulta/Servicios/', consultarServicios, name='ConsultarServicios'),
    path('Consulta/Servicios/Resultados/', resultadosServicios),
    #Consulta Empleados
    path('Consulta/Empleados/', consultarEmpleados, name='ConsultarEmpleados'),
    path('Consulta/Empleados/Resultados/', resultadosEmpleados),
]