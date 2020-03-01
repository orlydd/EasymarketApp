from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ciudades', views.ciudadView)
router.register('municipios', views.municipioView)
router.register('direcciones', views.direccionView)
router.register('sucursales', views.sucursalView)
router.register('productos', views.productoView)
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


urlpatterns = [
    path('', include(router.urls))
]
