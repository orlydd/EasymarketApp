from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('productos', views.productoView)
router.register('ciudades', views.ciudadView)
router.register('municipios', views.municipioView)
router.register('empleadosAuxiliar', views.empleadoAuxView)
router.register('productosAuxiliar', views.productoAuxView)
router.register('sucursalAuxiliar', views.sucursalAuxView)
router.register('suscripcionAuxiliar', views.suscripcionAuxView)
router.register('municipioAuxiliar', views.municipioAuxView)
router.register('ventaAuxiliar', views.ventaAuxView)
router.register('sucursales', views.sucursalView)
router.register('inventarios', views.inventarioView)
router.register('precioProducto', views.precioProductoView)
router.register('proveedores', views.proveedorView)
router.register('pagos', views.pagoView)
router.register('clientes', views.clienteView)
router.register('empleados', views.empleadoView)
router.register('ventas', views.ventaView)
router.register('ventas_Pago', views.ventaPagoView)
router.register('suscripciones', views.suscripcionView)
router.register('cajeros', views.cajeroView)
router.register('gerentes', views.gerenteView)
router.register('sucursales_inventarios', views.sucursal_inventarioView)
router.register('ventas_productos', views.venta_productoView)
router.register('proveedores_productos', views.proveedor_productoView)
router.register('tipoSuscripciones', views.tipoSuscripcionView)
router.register('categorias', views.categoriaView)
router.register('especialidades', views.especialidadView)





urlpatterns = [
    path('', include(router.urls))
]
