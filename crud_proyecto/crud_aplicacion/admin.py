from django.contrib import admin

from .models import *

admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(ciudad)
admin.site.register(municipio)
admin.site.register(cliente_direccion)
admin.site.register(proveedor)
admin.site.register(ciudad_proveedor)
admin.site.register(venta)
admin.site.register(informacion_venta)
admin.site.register(vendedor)
admin.site.register(proveedor_producto)
admin.site.register(categoria)
admin.site.register(categoria_producto)
admin.site.register(vendedor_venta)
admin.site.register(suscripcion)
admin.site.register(tipoSuscripcion)
admin.site.register(tipo_Suscripcion)
