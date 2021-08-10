from typing import Generic
from django.shortcuts import  render, redirect
from django.urls.base import reverse_lazy

from django.views import generic

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url =reverse_lazy("inv:categoria_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url =reverse_lazy("inv:categoria_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)
    
class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"    
    success_url =reverse_lazy("inv:categoria_list")

# PRODUCTO---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url =reverse_lazy("inv:producto_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url =reverse_lazy("inv:producto_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)
    
def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"

    if not producto:
        return redirect("inv:producto_list")

    if request.method == 'GET':
        contexto = {'obj' :producto}
    
    if request.method == 'POST':
        producto.estado=False
        producto.save()
        return redirect("inv:producto_list")

    return render(request, template_name, contexto)