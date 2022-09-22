from django.db import models

# Create your models here.
class Sucursal(models.Model):
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=120)
    codigoSucursal = models.IntegerField()
    correoSucursal = models.EmailField()

class Servicio(models.Model):
    codigoServicio = models.IntegerField()
    nombreServicio = models.CharField(max_length=50)
    descripcionServicio = models.CharField(max_length=200)
    unidadFacturacion = models.CharField(max_length=20)
    costoUnidad = models.FloatField()

class Empleado(models.Model):
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    codigoEmpleado = models.IntegerField()
    numeroIdentificacion = models.IntegerField()
    correo = models.EmailField()
