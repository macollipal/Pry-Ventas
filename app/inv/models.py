from enum import unique
from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(max_length=100, help_text='Descripción de la categoría', unique=True)

    def __str__(self) :
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural="Categorias"

#PRODUCTO        

class Producto(ClaseModelo):
    codigo= models.CharField(max_length=20, unique=True)
    codigo_barra = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    #marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    #u_medida = models.ForeignKey(UM, on_delete=models.CASCADE)
    #subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self) :
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name_plural="Productos"
        unique_together =('codigo', 'codigo_barra')