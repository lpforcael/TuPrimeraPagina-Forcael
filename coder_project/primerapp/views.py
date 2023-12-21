from django.shortcuts import render, redirect
from primerapp.models import Ciudad, Item, Usuario
from django.template import loader
from django.http import HttpResponse
from primerapp.forms import CiudadFormulario
#from primerapp.forms import UsuarioFormulario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def crear_ciudad(request):
#     ciudad = Ciudad(nombre_ciudad="New York", pais="USA")
    
#     ciudad.save()
    
#     template = loader.get_template("creacion_ciudad.html")
    
#     doc = template.render({"nombre": ciudad.nombre_ciudad})
    
#     return HttpResponse(doc)

@login_required(login_url = 'login')
def crear_item(request):
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_item = Item(
            ciudad = Ciudad.objects.all(),
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            costo = request.POST["costo"]
        )
        nuevo_item.save()
        return render(request, "index.html")
    
    return render(request, 'item_formulario.html')

@login_required(login_url = 'login')
def crear_ciudad(request):
    if request.method == "POST":
        nuevo_formulario = CiudadFormulario(request.POST)
        
        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nueva_ciudad = Ciudad(
                    nombre_ciudad=informacion["nombre_ciudad"],
                    pais=informacion["pais"],
                    imagen=informacion["imagen"]
                    )
                
            nueva_ciudad.save()
            return render(request, 'index.html', imagen)
    else:
        nuevo_formulario = CiudadFormulario()
        return render(request, 'ciudad_formulario.html', {"formulario": nuevo_formulario})
 
@login_required(login_url = 'login')    
def crear_usuario(request):
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_usuario = Usuario(
            nombre = request.POST["nombre"],
            nacionalidad = request.POST["nacionalidad"],
            edad = request.POST["edad"],
            password = request.POST["password"],
        )
        nuevo_usuario.save()
        return render(request, "index.html")
    
    return render(request, 'usuario_formulario.html')

@login_required(login_url = 'login')
def busqueda_en_bd(request):
    if request.GET.get("nombre_ciudad", False): # Uso el método .get() de diccionarios para obtener el nombre que recibo desde el html
                                         # Si dicho nombre no existe en el diccionario, entonces devuelve False y no entra en el if
        busqueda = request.GET["nombre_ciudad"]
        # Con Producto.objects.filter obtengo una lista de todos los elementos que tengan el nombre que ingresé por el formulario
        # __icontains viene de "if contains", con lo cual en lugar de buscar una coincidencia exacta, va a buscar cualquier elemento
        # que contenga el texto que ingresamos en la búsqueda.
        #lista_ciudades = Ciudad.objects.all()
        lista_ciudades = Ciudad.objects.filter(nombre_ciudad__icontains=busqueda)
        
        return render(request, 'busqueda.html', {'lista': lista_ciudades})
    
    return render(request, 'busqueda.html')

##CRUD ITEM y CIUDADES##

class CiudadListView(ListView):
    model = Ciudad
    context_object_name = "primerapp"
    template_name = "ciudad_lista.html"
    
class CiudadUpdateView(UpdateView):
    model = Ciudad
    template_name = "ciudad_editar.html"
    success_url = reverse_lazy('ciudad lista')
    fields = ['nombre_ciudad', 'pais', 'imagen']
    login_url = "login"
    
class CiudadDeleteView(DeleteView):
    model = Ciudad
    template_name = "ciudad_eliminar.html"
    success_url = reverse_lazy('ciudad lista')
    login_url = "login"

class ItemListView(ListView):
    model = Item
    context_object_name = "primerapp"
    template_name = "item_lista.html"

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "item_crear.html"
    success_url = reverse_lazy('item crear')
    fields = ['ciudad', 'nombre', 'descripcion', 'costo']
    login_url = "login"
       
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "item_editar.html"
    success_url = reverse_lazy('item lista')
    fields = ['ciudad', 'nombre', 'descripcion', 'costo']
    login_url = "login"

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "item_eliminar.html"
    success_url = reverse_lazy("item lista")
    login_url = "login"