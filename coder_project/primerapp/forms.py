from django import forms

class CiudadFormulario(forms.Form):
    nombre_ciudad = forms.CharField()
    pais = forms.CharField()
    imagen = forms.ImageField()

# class UsuarioFormulario(forms.Form):
#     nombre = forms.CharField()
#     nacionalidad = forms.CharField()
#     edad = forms.IntegerField()
#     password = forms.CharField()
    