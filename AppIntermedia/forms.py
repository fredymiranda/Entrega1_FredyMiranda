from django import forms

class CrearSucursal(forms.Form):
    paisF = forms.CharField(max_length=50, label='Pais:')
    ciudadF = forms.CharField(max_length=50, label='Ciudad:')
    direccionF = forms.CharField(max_length=120, label='Dirección:')
    codigoSucursalF = forms.IntegerField(label='Código Sucursal:')
    correoSucursalF = forms.EmailField(label='Correo Sucursal:')

class CrearServicio(forms.Form):
    codigoServicioF = forms.IntegerField(label='Código Servicio:')
    nombreServicioF = forms.CharField(max_length=50, label='Nombre Servicio:')
    descripcionServicioF = forms.CharField(max_length=200, label='Descripción Servicio:')
    unidadFacturacionF = forms.CharField(max_length=20, label='Unidad de Facturación:')
    costoUnidadF = forms.FloatField(label='Valor Unidad:')

class CrearEmpleado(forms.Form):
    nombresF = forms.CharField(max_length=35, label='Nombres:')
    apellidosF = forms.CharField(max_length=35, label='Apellidos:')
    codigoEmpleadoF = forms.IntegerField(label='Código de Empleado:')
    numeroIdentificacionF = forms.IntegerField(label='Número de Identificación:')
    correoF = forms.EmailField(label='Correo Electrónico:')
