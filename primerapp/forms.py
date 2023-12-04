from django import forms

class CiudadFormulario(forms.Form):
    nombre_ciudad = forms.CharField()
    pais = forms.CharField()

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    nacionalidad = forms.CharField()
    edad = forms.CharField()
    password = forms.CharField()
    