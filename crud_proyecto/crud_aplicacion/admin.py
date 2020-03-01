from django.contrib import admin

from .models import *

admin.site.register(ciudad)
admin.site.register(municipio)
admin.site.register(direccion)
admin.site.register(sucursal)
admin.site.register(producto)
admin.site.register(inventario)
admin.site.register(precioProducto)
admin.site.register(proveedor)
admin.site.register(pago)
admin.site.register(cliente)
admin.site.register(empleado)
admin.site.register(venta)
admin.site.register(ventaPago)
admin.site.register(suscripcion)
admin.site.register(cajero)
admin.site.register(gerente)
admin.site.register(sucursal_inventario)
admin.site.register(venta_Producto)
admin.site.register(proveedor_Producto)

