from django.shortcuts import render
from rest_framework import viewsets
from .models import ciudad, municipio, sucursal, producto, inventario, precioProducto, proveedor, pago, categoria, tipoSuscripcion, especialidad
from .models import cliente, empleado, venta, ventaPago, suscripcion, cajero, gerente, sucursal_inventario, venta_Producto, proveedor_Producto
from .serializers import ciudadSerializer, municipioSerializer, sucursalSerializer, productoSerializer, inventarioSerializer
from .serializers import precioProductoSerialiazer, proveedorSerializer, pagoSerializer, clienteSerializer, especialidadSerializer
from .serializers import gerenteSerializer,sucursal_inventarioSerializer, venta_productoSerializer, proveedor_productoSerializer
from .serializers import empleadoSerializer, ventaSerializer, ventaPagoSerializer, suscripcionSerializer, cajeroSerializer, categoriaSerializer, tipoSuscripcionSerializer

class ciudadView(viewsets.ModelViewSet):
    queryset = ciudad.objects.all()
    serializer_class = ciudadSerializer

class especialidadView(viewsets.ModelViewSet):
    queryset = especialidad.objects.all()
    serializer_class = especialidadSerializer

class municipioView(viewsets.ModelViewSet):
    queryset = municipio.objects.all()
    serializer_class = municipioSerializer

class tipoSuscripcionView(viewsets.ModelViewSet):
    queryset = tipoSuscripcion.objects.all()
    serializer_class = tipoSuscripcionSerializer

class categoriaView(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer

class sucursalView(viewsets.ModelViewSet):
    queryset = sucursal.objects.all()
    serializer_class = sucursalSerializer

class productoView(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = productoSerializer

class inventarioView(viewsets.ModelViewSet):
    queryset = inventario.objects.all()
    serializer_class = inventarioSerializer

class precioProductoView(viewsets.ModelViewSet):
    queryset = precioProducto.objects.all()
    serializer_class = precioProductoSerialiazer

class proveedorView(viewsets.ModelViewSet):
    queryset = proveedor.objects.all()
    serializer_class = proveedorSerializer

class pagoView(viewsets.ModelViewSet):
    queryset = pago.objects.all()
    serializer_class = pagoSerializer

class clienteView(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer

class empleadoView(viewsets.ModelViewSet):
    queryset = empleado.objects.all()
    serializer_class = empleadoSerializer

class ventaView(viewsets.ModelViewSet):
    queryset = venta.objects.all()
    serializer_class = ventaSerializer

class ventaPagoView(viewsets.ModelViewSet):
    queryset = ventaPago.objects.all()
    serializer_class = ventaPagoSerializer

class suscripcionView(viewsets.ModelViewSet):
    queryset = suscripcion.objects.all()
    serializer_class = suscripcionSerializer

class cajeroView(viewsets.ModelViewSet):
    queryset = cajero.objects.all()
    serializer_class = cajeroSerializer

class gerenteView(viewsets.ModelViewSet):
    queryset = gerente.objects.all()
    serializer_class = gerenteSerializer

class sucursal_inventarioView(viewsets.ModelViewSet):
    queryset = sucursal_inventario.objects.all()
    serializer_class = sucursal_inventarioSerializer

class venta_productoView(viewsets.ModelViewSet):
    queryset = venta_Producto.objects.all()
    serializer_class = venta_productoSerializer

class proveedor_productoView(viewsets.ModelViewSet):
    queryset = proveedor_Producto.objects.all()
    serializer_class = proveedor_productoSerializer
