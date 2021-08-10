from django.urls import path


from .views import ClienteView, ClienteNew, ClienteEdit, cliente_inactivar
    

urlpatterns = [

    path('Clientes/' , ClienteView.as_view(), name='cliente_list'),
    path('Clientes/new' , ClienteNew.as_view(), name='cliente_new'),
    path('Clientes/edit/<int:pk>' , ClienteEdit.as_view(), name='cliente_edit'),
    path('Clientes/inactivar/<int:id>' , cliente_inactivar, name='cliente_inactivar'),

    
]
