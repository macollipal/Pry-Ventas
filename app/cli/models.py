from enum import unique
from django.db import models

from bases.models import ClaseModelo


#CLIENTE       

class Cliente(ClaseModelo):
    codigo= models.CharField(max_length=20, unique=True)
    rut = models.CharField(max_length=200)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    fecha_nac = models.DateField(null=True, blank=True)
    
    #precio = models.FloatField(default=0)
    #existencia = models.IntegerField(default=0)
    #marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    #u_medida = models.ForeignKey(UM, on_delete=models.CASCADE)
    #subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self) :
        return '{}'.format(self.rut)

    def save(self):
        self.rut = self.rut.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural="Clientes"
        unique_together =('codigo', 'rut')