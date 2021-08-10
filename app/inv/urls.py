from django.urls import path


from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, \
    ProductoView, ProductoNew, ProductoEdit, producto_inactivar
    

urlpatterns = [
    path('categorias/' , CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new' , CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>' , CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>' , CategoriaDel.as_view(), name='categoria_del'),

    path('productos/' , ProductoView.as_view(), name='producto_list'),
    path('productos/new' , ProductoNew.as_view(), name='producto_new'),
    path('productos/edit/<int:pk>' , ProductoEdit.as_view(), name='producto_edit'),
    path('productos/inactivar/<int:id>' , producto_inactivar, name='producto_inactivar'),

    
]
