from django.contrib import admin

# Register your models here.

from primerapp.models import Ciudad, Item, Usuario

admin.site.register(Ciudad)
admin.site.register(Item)
admin.site.register(Usuario)