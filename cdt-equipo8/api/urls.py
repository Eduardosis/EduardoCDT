from django.urls import path
from .views import *
from api.views import (
	UserRegistrationAPIView,
	UserLoginAPIView,
	UserViewAPI,
	UserLogoutViewAPI,
   # UserChangePasswordView
)

urlpatterns = [
    
    path('ee-serviciopaqueteria/', EeServiciopaqueteriaListCreate.as_view(), name='ee_serviciopaqueteria_list_create'),
    path('ee-serviciopaqueteria/<int:pk>/', EeServiciopaqueteriaRetrieveUpdateDestroy.as_view(), name='ee_serviciopaqueteria_detail'),

    path('p-empresa/', PEmpresaListCreate.as_view(), name='p_empresa_list_create'),
    path('p-empresa/<str:pk>/', PEmpresaRetrieveUpdateDestroy.as_view(), name='p_empresa_detail'),

    path('agr-categoriausuario/', AgrCategoriausuarioListCreate.as_view(), name='agr_categoriausuario_list_create'),
    path('agr-categoriausuario/<int:pk>/', AgrCategoriausuarioRetrieveUpdateDestroy.as_view(), name='agr_categoriausuario_detail'),

    path('agr-usuario/', AgrUsuarioListCreate.as_view(), name='agr_usuario_list_create'),
    path('agr-usuario/<int:pk>/', AgrUsuarioRetrieveUpdateDestroy.as_view(), name='agr_usuario_detail'),

    path('agr-almacen/', AgrAlmacenListCreate.as_view(), name='agr_almacen_list_create'),
    path('agr-almacen/<str:pk>/', AgrAlmacenRetrieveUpdateDestroy.as_view(), name='agr_almacen_detail'),

    path('p-proveedor/', PProveedorListCreate.as_view(), name='p_proveedor_list_create'),
    path('p-proveedor/<int:pk>/', PProveedorRetrieveUpdateDestroy.as_view(), name='p_proveedor_detail'),

    path('p-clientesp/', PClientesPListCreate.as_view(), name='p_clientesp_list_create'),
    path('p-clientesp/<int:pk>/', PClientesPRetrieveUpdateDestroy.as_view(), name='p_clientesp_detail'),

    path('agr-categoriaproducto/', AgrCategoriaproductoListCreate.as_view(), name='agr_categoriaproducto_list_create'),
    path('agr-categoriaproducto/<int:pk>/', AgrCategoriaproductoRetrieveUpdateDestroy.as_view(), name='agr_categoriaproducto_detail'),

    path('agr-almacen-proveedor/', AgrAlmacenProveedorListCreate.as_view(), name='agr_almacen_proveedor_list_create'),
    path('agr-almacen-proveedor/<int:pk>/', AgrAlmacenProveedorRetrieveUpdateDestroy.as_view(), name='agr_almacen_proveedor_detail'),

    path('agr-productos/', AgrProductosListCreate.as_view(), name='agr_productos_list_create'),
    path('agr-productos/<str:pk>/', AgrProductosRetrieveUpdateDestroy.as_view(), name='agr_productos_detail'),

    path('agr-detalleproductos/', AgrDetalleproductosListCreate.as_view(), name='agr_detalleproductos_list_create'),
    path('agr-detalleproductos/<int:pk>/', AgrDetalleproductosRetrieveUpdateDestroy.as_view(), name='agr_detalleproductos_detail'),

    path('agr-fotos/', AgrFotosListCreate.as_view(), name='agr_fotos_list_create'),
    path('agr-fotos/<int:pk>/', AgrFotosRetrieveUpdateDestroy.as_view(), name='agr_fotos_detail'),

    path('agr-categoria-producto/', AgrCategoriaProductoListCreate.as_view(), name='agr_categoria_producto_list_create'),
    path('agr-categoria-producto/<int:pk>/', AgrCategoriaProductoRetrieveUpdateDestroy.as_view(), name='agr_categoria_producto_detail'),

    path('agr-producto-proveedor/', AgrProductoProveedorListCreate.as_view(), name='agr_producto_proveedor_list_create'),
    path('agr-producto-proveedor/<int:pk>/', AgrProductoProveedorRetrieveUpdateDestroy.as_view(), name='agr_producto_proveedor_detail'),

    path('agr-solicitar-producto/', AgrSolicitarProductoListCreate.as_view(), name='agr_solicitar_producto_list_create'),
    path('agr-solicitar-producto/<int:pk>/', AgrSolicitarProductoRetrieveUpdateDestroy.as_view(), name='agr_solicitar_producto_detail'),

    path('agr-reporteproducto-falla/', AgrReporteproductoFallaListCreate.as_view(), name='agr_reporteproducto_falla_list_create'),
    path('agr-reporteproducto-falla/<int:pk>/', AgrReporteproductoFallaRetrieveUpdateDestroy.as_view(), name='agr_reporteproducto_falla_detail'),

    path('agr-reporte-producto-recibidos/', AgrReporteProductoRecibidosListCreate.as_view(), name='agr_reporte_producto_recibidos_list_create'),
    path('agr-reporte-producto-recibidos/<int:pk>/', AgrReporteProductoRecibidosRetrieveUpdateDestroy.as_view(), name='agr_reporte_producto_recibidos_detail'),

    path('ee-almacen-paqueteria/', EeAlmacenPaqueteriaListCreate.as_view(), name='ee_almacen_paqueteria_list_create'),
    path('ee-almacen-paqueteria/<int:pk>/', EeAlmacenPaqueteriaRetrieveUpdateDestroy.as_view(), name='ee_almacen_paqueteria_detail'),

    path('p-ordenenvio/', POrdenenvioListCreate.as_view(), name='p_ordenenvio_list_create'),
    path('p-ordenenvio/<int:pk>/', POrdenenvioRetrieveUpdateDestroy.as_view(), name='p_ordenenvio_detail'),

    path('ee-ruta/', EeRutaListCreate.as_view(), name='ee_ruta_list_create'),
    path('ee-ruta/<int:pk>/', EeRutaRetrieveUpdateDestroy.as_view(), name='ee_ruta_detail'),

    path('ee-envio/', EeEnvioListCreate.as_view(), name='ee_envio_list_create'),
    path('ee-envio/<int:pk>/', EeEnvioRetrieveUpdateDestroy.as_view(), name='ee_envio_detail'),

    path('ee-entrega/', EeEntregaListCreate.as_view(), name='ee_entrega_list_create'),
    path('ee-entrega/<int:pk>/', EeEntregaRetrieveUpdateDestroy.as_view(), name='ee_entrega_detail'),
    
    path('ee-camion/', EeCamionListCreate.as_view(), name='ee_camion_list_create'),
    path('ee-camion/<int:pk>/', EeCamionRetrieveUpdateDestroy.as_view(), name='ee_camion_detail'),
    
    path('ee-repartidor/', EeRepartidorListCreate.as_view(), name='ee_repartidor_list_create'),
    path('ee-repartidor/<int:pk>/', EeRepartidorRetrieveUpdateDestroy.as_view(), name='ee_repartidor_detail'),

    path('agr-reporteentrega/', AgrReporteEntregaListCreate.as_view(), name='agr_reporteentrega_list_create'),
    path('agr-reporteentrega/<int:pk>/', AgrReporteEntregaRetrieveUpdateDestroy.as_view(), name='agr_reporteentrega_detail'),

    path('agr-reporteenvio/', AgrReporteEnvioListCreate.as_view(), name='agr_reporteenvio_list_create'),
    path('agr-reporteenvio/<int:pk>/', AgrReporteEnvioRetrieveUpdateDestroy.as_view(), name='agr_reporteenvio_detail'),

    path('agr-reporte-recoleccion/', AgrReporteRecoleccionListCreate.as_view(), name='agr_reporte_recoleccion_list_create'),
    path('agr-reporte-recoleccion/<int:pk>/', AgrReporteRecoleccionRetrieveUpdateDestroy.as_view(), name='agr_reporte_recoleccion_detail'),

    path('agr-productos-historial/', AgrProductosHistorialListCreate.as_view(), name='agr_productos_historial_list_create'),
    path('agr-productos-historial/<int:pk>/', AgrProductosHistorialRetrieveUpdateDestroy.as_view(), name='agr_productos_historial_detail'),



    ##Derian's extra extra extra stuff

    path('user/register/', UserRegistrationAPIView.as_view()),
	path('user/login/', UserLoginAPIView.as_view()),
	path('user/', UserViewAPI.as_view()),
	path('user/logout/', UserLogoutViewAPI.as_view()),
    path('check-provider-status/', CheckProviderStatusAPIView.as_view(), name='check-provider-status'),
    path('get-provider-id/', GetProviderIdAPIView.as_view(), name='get-provider-id'),
    path('user/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('get-provider-products/', GetProviderProductsAPIView.as_view(), name='get-provider-products'),
    path('get-provider-clients/', GetProviderClientsAPIView.as_view(), name='get-provider-clients'),
    path('get-provider-orders/', GetProviderOrdersAPIView.as_view(), name='get-provider-orders'),
]