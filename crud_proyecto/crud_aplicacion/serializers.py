from rest_framework import serializers
from .models import ciudad, municipio, sucursal, producto, inventario, precioProducto, proveedor, pago, tipoSuscripcion, categoria, especialidad
from .models import cliente, empleado, venta, ventaPago, suscripcion, cajero, gerente, sucursal_inventario, venta_Producto, proveedor_Producto

class ciudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciudad
        fields = ('id', 'nombre')

class municipioSerializer(serializers.ModelSerializer):
    ciudadID = ciudadSerializer()
    class Meta:
        model = municipio
        fields = ('id', 'nombre', 'ciudadID')

class sucursalSerializer(serializers.ModelSerializer):
    municipioID = municipioSerializer()
    class Meta:
        model = sucursal
        fields = ('id', 'nombre', 'municipioID', 'activo')

class categoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ('id', 'nombre')

class productoSerializer(serializers.ModelSerializer):
    categoriaID = categoriaSerializer()
    class Meta:
        model = producto
        fields = ('id', 'nombre', 'categoriaID')

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
        fields = ('id', 'nombre', 'telefono', 'ciudadID', 'activo')

class pagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pago
        fields = ('id', 'monto', 'instrumento')

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ('id', 'cedula', 'nombre', 'apellido', 'telefono')

class empleadoSerializer(serializers.ModelSerializer):
    sucursalID = sucursalSerializer()
    class Meta:
        model = empleado
        fields = ('id', 'cedula', 'nombre', 'apellido', 'fechaNacimiento', 'telefono', 'sucursalID', 'activo')

class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta
        fields = ('id', 'fechaVenta', 'clienteID', 'empleadoID')

class ventaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ventaPago
        fields = ('ventaID', 'pagoID')

class tipoSuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipoSuscripcion
        fields = ('id', 'nombre')

class suscripcionSerializer(serializers.ModelSerializer):
    tipoID = tipoSuscripcionSerializer()
    clienteID = clienteSerializer()
    class Meta:
        model = suscripcion
        fields = ('id', 'clienteID', 'fechaSuscripcion', 'tipoID', 'activo')

class cajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = cajero
        fields = ('empleadoID', 'nroCaja')

class especialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = especialidad
        fields = ('id', 'especialidadID')

class gerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = gerente
        fields = ('empleadoID', 'especialidadID')

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