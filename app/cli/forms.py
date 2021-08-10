from django import forms
#from django.db import models
#from django.forms import fields, widgets
from .models import Cliente


class ClienteForm(forms.ModelForm):
    fecha_nac = forms.DateInput()
    class Meta:
        model = Cliente
        fields = ['codigo','rut','nombres', 'apellidos', 'direccion', 'fecha_nac','estado']
        exclude =['created_date','modified_date','created_by' ,'modified_by']
        widget = {'rut': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        #self.fields['ultima_compra'].widget.attrs['readonly'] = True
        #self.fields['existencia'].widget.attrs['readonly'] = True
