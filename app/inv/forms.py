from django import forms
#from django.db import models
#from django.forms import fields, widgets
from .models import Categoria, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripcion de la Categoria",
                'estado': "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        
#PRODUCTO----------------------------------------------------------

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = ['codigo','codigo_barra','descripcion', 'estado', 'precio', 'existencia','ultima_compra', 'marca','subcategoria', 'u_medida']
        fields = ['codigo','codigo_barra','descripcion', 'estado', 'precio', 'existencia','ultima_compra']
        exclude =['created_date','modified_date','created_by' ,'modified_by']
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True
