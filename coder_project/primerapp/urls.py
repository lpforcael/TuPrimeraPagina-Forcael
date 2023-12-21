from django.urls import path
from primerapp.views import crear_ciudad, crear_usuario, busqueda_en_bd, CiudadListView, ItemCreateView, ItemListView, ItemUpdateView, ItemDeleteView, CiudadUpdateView, CiudadDeleteView
urlpatterns = [
    path('crear_ciudad/', crear_ciudad, name='crear ciudad'),
    path('item_lista/', ItemListView.as_view(), name='item lista'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('busqueda_bd/', busqueda_en_bd, name='busqueda_en_bd'),
    path('ciudad_lista/', CiudadListView.as_view(), name='ciudad lista'),
    path('item_crear/', ItemCreateView.as_view(), name='item crear'),
    path('<pk>/editar/', ItemUpdateView.as_view(), name='item editar'),
    path('<pk>/eliminar/', ItemDeleteView.as_view(), name='item eliminar'),
    path('<pk>/modificar/', CiudadUpdateView.as_view(), name='ciudad editar'),
    path('<pk>/quitar/', CiudadDeleteView.as_view(), name='ciudad eliminar'),
]