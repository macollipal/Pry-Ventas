from typing import Generic
from django.shortcuts import  render, redirect
from django.urls.base import reverse_lazy

from django.views import generic

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Cliente
from .forms import ClienteForm

class ClienteView(LoginRequiredMixin, generic.ListView):
    model = Cliente
    template_name = "cli/cliente_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ClienteNew(LoginRequiredMixin, generic.CreateView):
    model = Cliente
    template_name = "cli/cliente_form.html"
    context_object_name = "obj"
    form_class = ClienteForm
    success_url =reverse_lazy("cli:cliente_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        return super().form_valid(form)

class ClienteEdit(LoginRequiredMixin, generic.UpdateView):
    model = Cliente
    template_name = "cli/cliente_form.html"
    context_object_name = "obj"
    form_class = ClienteForm
    success_url =reverse_lazy("cli:cliente_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)
    
def cliente_inactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()
    contexto={}
    template_name="cli/cliente_del.html"

    if not cliente:
        return redirect("cli:cliente_list")

    if request.method == 'GET':
        contexto = {'obj' :cliente}
    
    if request.method == 'POST':
        cliente.estado=False
        cliente.save()
        return redirect("cli:cliente_list")

    return render(request, template_name, contexto)