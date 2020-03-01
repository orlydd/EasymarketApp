from django.db import models

class ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=400, blank=False)

    class Meta:
        verbose_name = 'ciudad'
        verbose_name_plural = 'ciudades'

    def __str__(self):
        
        return f'{self.nombre}'

class municipio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=400, blank=False)

    def __str__(self):
        
        return f'{self.nombre}'

class direccion(models.Model):
    id = models.AutoField(primary_key=True)
    ciudadID = models.ForeignKey(
        ciudad, on_delete=models.CASCADE
    ) 
    municipioID = models.ForeignKey(
        municipio, on_delete=models.CASCADE
    )
    calle = models.CharField(max_length=500, blank=False)

    class Meta:
        verbose_name = 'direccion'
        verbose_name_plural = 'direcciones'

    def __str__(self):
        
        return f'Sucursal en {self.ciudadID.nombre} : {self.municipioID.nombre}, {self.calle}' 


class sucursal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=400, blank=False)
    direccionID = models.ForeignKey(
        direccion, on_delete=models.CASCADE
    )
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'

    def __str__(self):
        
        return f'{self.nombre}'

class producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=400, blank=False)
    categoria = models.CharField(max_length=400, blank=False)
    def __str__(self):
        
        return f'{self.nombre}'

class inventario(models.Model):
    id = models.AutoField(primary_key=True)
    productoID = models.ForeignKey(
        producto, on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(blank=False, default='')

    def __str__(self): 
        return f'Inventario {self.id}'

class precioProducto(models.Model):
    productoID = models.ForeignKey(
        producto, on_delete=models.CASCADE
    )
    monto = models.DecimalField(max_digits=10, decimal_places= 2, blank=False, default='')
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        
        return f'Precio de  {self.productoID.nombre}'

class proveedor(models.Model):
    id = models.AutoField (primary_key = True)
    nombre = models.CharField(max_length=400, blank=False)
    telefono = models.CharField(max_length=15, blank=False, default='')
    direccionID = models.ForeignKey(
        direccion, on_delete= models.CASCADE
    )
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'

    def __str__(self):
        
        return f'{self.nombre}'

class pago(models.Model):
    id = models.AutoField (primary_key = True)
    monto = models.DecimalField(max_digits=10, decimal_places= 2, blank=False, default='')
    instrumento = models.CharField(max_length=400, blank=False)
    def __str__(self):
        
        return f'Pago Nro {self.id}'

class cliente(models.Model):
    id = models.AutoField (primary_key = True)
    cedula = models.IntegerField(unique=True, blank=False, default='')
    nombre = models.CharField(max_length=400, blank=False)
    apellido = models.CharField(max_length=400, blank=False)
    telefono = models.CharField(max_length=12, blank=False, default='')
    direccionID = models.ForeignKey(
        direccion, on_delete= models.CASCADE
    )
    def __str__(self):
        
        return f'{self.nombre} {self.apellido}'

class empleado(models.Model):
    id = models.AutoField (primary_key = True)
    cedula = models.IntegerField(unique=True, blank=False, default='')
    nombre = models.CharField(max_length=400, blank=False)
    apellido = models.CharField(max_length=400, blank=False)
    fechaNacimiento = models.CharField(max_length=12, blank=False, default="")
    telefono = models.CharField(max_length=12, blank=False, default='')
    direccionID = models.ForeignKey(
        direccion, on_delete= models.CASCADE
    )
    sucursalID = models.ForeignKey(
        sucursal, on_delete= models.CASCADE
    )
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        
        return f'{self.nombre} {self.apellido}'

class venta(models.Model):
    id = models.AutoField (primary_key = True)
    fechaVenta = models.DateTimeField(auto_now_add=True)
    clienteID = models.ForeignKey(
        cliente, on_delete=models.CASCADE
    )
    empleadoID = models.ForeignKey(
        empleado, on_delete=models.CASCADE
    )

    def __str__(self):
        
        return f'Venta de {self.clienteID.nombre} {self.clienteID.apellido}'

class ventaPago(models.Model):
    ventaID = models.ForeignKey(
        venta, on_delete= models.CASCADE
    )
    pagoID = models.ForeignKey(
        pago, on_delete= models.CASCADE
    )
    def __str__(self):
        
        return f'Pago de la venta {self.ventaID.id}'

class suscripcion(models.Model):
    id = models.AutoField (primary_key = True)
    clienteID = models.ForeignKey(
        cliente, on_delete=models.CASCADE
    )
    fechaSuscripcion = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=400, blank=False)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'suscripcion'
        verbose_name_plural = 'suscripciones'

    def __str__(self):
        # pylint: disable=E1101
        return f'suscripcion de {self.clienteID.nombre} {self.clienteID.apellido}'

class cajero(models.Model):
    empleadoID = models.ForeignKey(
        empleado, on_delete=models.CASCADE
    )
    nroCaja = models.PositiveIntegerField(blank=False, default='')
    def __str__(self):
        
        return f'{self.empleadoID.nombre} {self.empleadoID.apellido}'

class gerente(models.Model):
    empleadoID = models.ForeignKey(
        empleado, on_delete=models.CASCADE
    )
    especialidad = models.CharField(max_length=400, blank=False)

    def __str__(self):
        
        return f'{self.empleadoID.nombre} {self.empleadoID.apellido}'

class sucursal_inventario(models.Model):
    sucursalID = models.ForeignKey(
        sucursal, on_delete=models.CASCADE
    )
    inventarioID = models.ForeignKey(
        inventario, on_delete=models.CASCADE
    )
    def __str__(self):
        
        return f'Inventario de la sucursal {self.sucursalID.nombre}'

class venta_Producto(models.Model):
    ventaID = models.ForeignKey(
        venta, on_delete=models.CASCADE
    )
    productoID = models.ForeignKey(
        producto, on_delete=models.CASCADE
    )
    cantidad = models.PositiveIntegerField(blank=False, default= '')

    def __str__(self):
        
        return f'Venta {self.ventaID.id}'

class proveedor_Producto(models.Model):
    proveedorID = models.ForeignKey(
        proveedor, on_delete=models.CASCADE
    )
    productoID = models.ForeignKey(
        producto, on_delete=models.CASCADE
    )
    def __str__(self):
        
        return f'Proovedor {self.proveedorID.nombre}, producto {self.productoID.nombre}'

