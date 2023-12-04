from django.urls import path
from primerapp.views import crear_ciudad, crear_item, crear_usuario

urlpatterns = [
    path('crear_ciudad/', crear_ciudad, name='crear ciudad'),
    path('crear_item/', crear_item, name='crear_item'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
]