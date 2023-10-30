from django.contrib import admin
from .models import Ciudad, Estado, Operacion, Propiedad
# Register your models here.

admin.site.register(Ciudad)
admin.site.register(Estado)
admin.site.register(Operacion)
admin.site.register(Propiedad)
