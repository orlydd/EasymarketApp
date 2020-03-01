from rest_framework import serializers
from .models import ciudad, municipio, direccion, sucursal, producto, inventario, precioProducto, proveedor, pago
from .models import cliente, empleado, venta, ventaPago, suscripcion, cajero, gerente, sucursal_inventario, venta_Producto, proveedor_Producto

class ciudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudad
        fields = ('id', 'nombre')

class municipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = municipio
        fields = ('id', 'nombre')

class direccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = direccion
        fields = ('id', 'ciudadID', 'municipioID')

class sucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = sucursal
        fields = ('id', 'nombre', 'direccionID', 'activo')

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ('id', 'nombre', 'categoria')

class inventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = inventario
        fields = ('id', 'productoID', 'cantidad')

class precioProductoSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = precioProducto
        fields = ('productoID', 'monto', 'fecha')

class proveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor
        fields = ('id', 'nombre', 'telefono', 'direccionID', 'activo')

class pagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pago
        fields = ('id', 'monto', 'instrumento')

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ('id', 'cedula', 'nombre', 'apellido', 'telefono', 'direccionID')

class empleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleado
        fields = ('id', 'cedula', 'nombre', 'apellido', 'fechaNacimiento', 'telefono', 'direccionID', 'sucursalID', 'activo')

class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta
        fields = ('id', 'fechaVenta', 'clienteID', 'empleadoID')

class ventaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ventaPago
        fields = ('ventaID', 'pagoID')

class suscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = suscripcion
        fields = ('id', 'clienteID', 'fechaSuscripcion', 'tipo', 'activo')

class cajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = cajero
        fields = ('empleadoID', 'nroCaja')

class gerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = gerente
        fields = ('empleadoID', 'especialidad')

class sucursal_inventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = sucursal_inventario
        fields = ('sucursalID', 'inventarioID')

class venta_productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta_Producto
        fields = ('ventaID', 'productoID', 'cantidad')

class proveedor_productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor_Producto
        fields = ('proveedorID', 'productoID')