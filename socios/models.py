from random import choices
from django.db import models
from pkg_resources import require

# Create your models here.

class Socio(models.Model):

    OCUPACION_CHOICES = [
        ('E', 'Estudiante'),
        ('J', 'Jubilado'),
        ('T', 'Trabajador'),
        ('O', 'Otra/No especifica')
    ]
    
    ESTADOS = [
        #('A', 'Activo'),
        #('I', 'Inactivo')
        ('0', 'Ingreso sin pago'),
        ('1', 'Al dia'),
        ('2', 'Debe'),
        ('3', 'Suspendido - Eliminado - Por eliminar')
    ]
    
    PAGOS = [
        ('A', 'Al dia'),
        ('D', 'Deuda')
    ]
    
    ESTABLECIMIENTO_CHOICES = [
        ('s', 'Socio sede')
    ]
    
    rut = models.CharField(unique=True, max_length=10, blank=False)
    dv = models.CharField(max_length=1, blank=True)
    correo = models.CharField(max_length=50, blank=False)
    nombres = models.CharField(max_length=50, blank=False)
    apellidos = models.CharField(max_length=50, blank=False)
    direccion = models.CharField(max_length=200, blank=False)
    telefono = models.CharField(max_length=9)
    foto = models.ImageField(upload_to='images/', null=True)
    fecha_nacimiento = models.DateField()
    ocupacion = models.CharField(choices=OCUPACION_CHOICES, max_length=1)
    estado = models.CharField(choices=ESTADOS, max_length=1, default='A')
    numero_socio = models.CharField(max_length=10, blank=True)
    deuda = models.CharField(max_length=1, choices=PAGOS, blank=True)
    rut_empresa = models.CharField(max_length=10, null=True)
    establecimiento = models.CharField(max_length=1, choices=ESTABLECIMIENTO_CHOICES, default='s')
    
    
class Cuota(models.Model):
    ESTADO_CHOICES = [
        ('p', 'Pagada'),
        ('n', 'No pagada')
    ]
    
    MES_CHOICES = [
        ('3', 'Marzo'),
        ('4', 'Abril'),
        ('5', 'Mayo'),
        ('6', 'Junio'),
        ('7', 'Julio'),
        ('8', 'Agosto'),
        ('9', 'Septiembre'),
        ('10', 'Octubre'),
        ('11', 'Noviembre'),
        ('12', 'Diciembre'),
    ]
    
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=False)
    mes = models.CharField(choices=MES_CHOICES, max_length=2)
    anio = models.IntegerField(blank=False, null=False)
    monto = models.IntegerField(blank=False, null=False)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=1, blank=False, null=False)
    
class Pago(models.Model):
    
    PAGO_CHOICES = [
        #('c', 'Credencial'),
        #('m', 'Mensualidad')
        ('100', 'Cuota social'),
        ('320', 'Cuota inscripcion'),
        ('110', 'Cuota familiar'),
        ('300', 'Abono'),
        ('322', 'Credencial'),
    ]
    
    MEDIOPAGO_CHOICES = [
        #('p', 'Descuento por planilla'),
        #('e', 'Efectivo'),
        #('d', 'Debito'),
        #('c', 'Credito'),
        #('h', 'Cheque'),
        #('w', 'Pago web')
        ('10', 'Efectivo'),
        ('20', 'Cheque'),
        ('30', 'Redcompra'),
        ('40', 'Credito'),
        ('50', 'Transferencia'),
        ('60', 'Master'),
        
    ]

     
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=False)
    cuota = models.ForeignKey(Cuota, on_delete=models.CASCADE, null=True)
    monto = models.IntegerField(blank=False, null=False)
    num_doc = models.CharField(max_length=20, blank=True, null=True)
    tipo_pago = models.CharField(choices=PAGO_CHOICES, max_length=3, blank=False, null=False)
    medio_pago = models.CharField(choices=MEDIOPAGO_CHOICES, max_length=2, blank=False, null=False)
    fecha_pago = models.DateField(blank=False, null=False)
 
 