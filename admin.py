from django.contrib import admin
from .models import projet, usuarios, instituciones
# Register your models here.
admin.site.register(projet)
admin.site.register(instituciones)
admin.site.register(usuarios)