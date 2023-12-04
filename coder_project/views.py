from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def saludo(request):
#     return HttpResponse("Hola comision 56050")

# def ver_comision(request):
#     nro_comision = 56050
    
#     diccionario = {"numero_comision": nro_comision}
    
#     template = loader.get_template("template.html")
    
#     doc = template.render(diccionario)
    
#     return HttpResponse(doc)

def pag_principal(request):
    return render(request, "index.html")