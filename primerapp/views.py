from django.shortcuts import render
from primerapp.models import Ciudad, Item, Usuario
from django.template import loader
from django.http import HttpResponse
from primerapp.forms import CiudadFormulario
from primerapp.forms import UsuarioFormulario

# Create your views here.

def crear_ciudad(request):
    ciudad = Ciudad(nombre_ciudad="New York", pais="USA")
    
    ciudad.save()
    
    template = loader.get_template("creacion_ciudad.html")
    
    doc = template.render({"nombre": ciudad.nombre_ciudad})
    
    return HttpResponse(doc)

def crear_item(request):
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_item = Item(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            costo_mensual = request.POST["costo_mensual"]
        )
        nuevo_item.save()
        return render(request, "index.html")
    
    return render(request, 'item_formulario.html')

def crear_ciudad(request):
    if request.method == "POST":
        nuevo_formulario = CiudadFormulario(request.POST)
        
        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nueva_ciudad = Ciudad(
                    nombre_ciudad=informacion["nombre_ciudad"],
                    pais=informacion["pais"],
                    )
                
            nueva_ciudad.save()
            return render(request, 'index.html')
    else:
        nuevo_formulario = CiudadFormulario()
        return render(request, 'ciudad_formulario.html', {"formulario": nuevo_formulario})
    
def crear_usuario(request):
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_usuario = Usuario(
            nombre = request.POST["nombre"],
            nacionalidad = request.POST["nacionalidad"],
            edad = request.POST["edad"],
            password = request.POST["password"]
        )
        nuevo_usuario.save()
        return render(request, "index.html")
    
    return render(request, 'usuario_formulario.html')
