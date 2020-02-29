from django.db import models



#Tabla de clientes
class cliente(models.Model):
    id = models.AutoField (primary_key = True)
    nombre = models.CharField(max_length=400, blank=False)
    apellido = models.CharField(max_length=400, blank=False)
    cedula = models.IntegerField (unique = True, blank=False)
    telefono = models.CharField(max_length=12, blank=False, default="")

    def __str__(self):
        
        return f'{self.nombre} {self.apellido}'

#Tabla de municipios
class municipio(models.Model):
    id = models.AutoField (primary_key = True)
    nombre = models.CharField(max_length=400, blank=False)

    def __str__(self):
        return self.nombre

#Tabla de ciudades
class ciudad(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=500, blank=False)

    class Meta:
        verbose_name = 'ciudad'
        verbose_name_plural = 'ciudades'

    def __str__(self):
        return self.nombre

#Tabla relacionando los clientes con la ciudad y municipio donde viven
class cliente_direccion(models.Model):
    clienteID = models.ForeignKey(
        cliente, on_delete=models.CASCADE
    )
    ciudadID = models.ForeignKey(
        ciudad, on_delete=models.CASCADE
    )
    municipioID = models.ForeignKey(
        municipio, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'cliente_direccion'
        verbose_name_plural = 'cliente_direcciones'

    def __str__(self):
        # pylint: disable=E1101
        nombre = self.clienteID.nombre
        apellido = self.clienteID.apellido
        return f'{nombre} {apellido}'

#Tabla de productos
class producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=300, blank=False)
    precioUnidad = models.DecimalField(max_digits=10, decimal_places=2, default='0',blank=False)
    cantidad = models.IntegerField(default='0', blank=False)

    def __str__(self):
        return self.nombre

#Tabla de proveedores
class proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=400, blank=False)
    telefono = models.CharField(max_length=12, blank=False, default="")
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'

    def __str__(self):
        return self.nombre

#Tabla relacionando los proveedores con las ciudad donde se encuentran
class ciudad_proveedor(models.Model):
    proveedorID = models.ForeignKey(
        proveedor, on_delete= models.CASCADE
    )
    ciudadID = models.ForeignKey(
        ciudad, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'ciudad_proveedor'
        verbose_name_plural = 'ciudad_proveedores'

    def __str__(self):
        # pylint: disable=E1101
        nombreProveedor = self.proveedorID.nombre
        return f'{nombreProveedor}'

#Tabla de ventas
class venta(models.Model):
    id = models.AutoField(primary_key=True)
    fechaVenta = models.DateTimeField(auto_now_add=True)
    clienteID = models.ForeignKey(
        cliente, on_delete= models.CASCADE
    )

    def __str__(self):
        # pylint: disable=E1101
        nombreCliente = self.clienteID.nombre
        apellidoCliente = self.clienteID.apellido
        fecha = self.fechaVenta
        return f'{nombreCliente} {apellidoCliente} {fecha}'

#Tabla relacionando los productos comprados con el id de la venta realizada
class informacion_venta(models.Model):
    ventaID = models.ForeignKey(
        venta, on_delete= models.CASCADE
    )
    productoID = models.ForeignKey(
        producto, on_delete=models.CASCADE
    )
    cantidad = models.IntegerField(blank=False)

    def __str__(self):
        # pylint: disable=E1101
        return f'venta {self.ventaID.id}'

#Tabla de vendedores
class vendedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=400, blank=False)
    apellido = models.CharField(max_length=400, blank=False)
    cedula = models.IntegerField (unique = True, blank=False)
    telefono = models.CharField(max_length=12, blank=False, default="")
    fechaNacimiento = models.CharField(max_length=12, blank=False, default="")
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

#Tabla de categorias
class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=400, blank=False)

    def __str__(self):
        return self.nombre

#Tabla relacionando los proveedores con los productos que traen
class proveedor_producto(models.Model):
    productoID = models.ForeignKey(
        producto, on_delete=models.CASCADE
    )
    proveedorID = models.ForeignKey(
        proveedor, on_delete=models.CASCADE
    )

    def __str__(self):
        # pylint: disable=E1101
        return f'proveedor de {self.productoID.nombre}'

#Tabla relacionando el vendedor con la venta que realizo
class vendedor_venta(models.Model):
    vendedorID = models.ForeignKey(
        vendedor, on_delete=models.CASCADE
    )
    ventaID = models.ForeignKey(
        venta, on_delete=models.CASCADE
    )

    def __str__(self):
        # pylint: disable=E1101
        return f'venta {self.ventaID.id}'

#Tabla relacionando el producto con la categoria a la que pertenece
class categoria_producto(models.Model):
    categoriaID = models.ForeignKey(
        categoria, on_delete=models.CASCADE
    )
    productoID = models.ForeignKey(
        producto, on_delete=models.CASCADE
    )

    def __str__(self):
        # pylint: disable=E1101
        return f'categoria de {self.productoID.nombre}'

#Tabla de suscripciones
class suscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    clienteID = models.ForeignKey(
        cliente, on_delete=models.CASCADE
    )
    fechaSuscricion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'suscripcion'
        verbose_name_plural = 'suscripciones'

    def __str__(self):
        # pylint: disable=E1101
        return f'suscripcion de {self.clienteID.nombre} {self.clienteID.apellido}'

#Tabla que indica el tipo de suscripciones que existen
class tipoSuscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    nombreTipo = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'tipoSuscripcion'
        verbose_name_plural = 'tipoSuscripciones'

    def __str__(self):
        # pylint: disable=E1101
        return self.nombreTipo

#Tabla relacionando una suscripcion con el tipo de suscripcion que es
class tipo_Suscripcion(models.Model):
    suscripcionID = models.ForeignKey(
        suscripcion, on_delete=models.CASCADE
    )
    tipoID = models.ForeignKey(
        tipoSuscripcion, on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = 'tipo_suscripcion'
        verbose_name_plural = 'tipo_suscripciones'

    def __str__(self):
        # pylint: disable=E1101
        return f'tipo de suscripcion de {self.suscripcionID.clienteID.nombre} {self.suscripcionID.clienteID.apellido}'





