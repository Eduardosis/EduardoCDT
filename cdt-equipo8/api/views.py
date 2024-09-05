from rest_framework import generics
from .models import *
from .serializers import *
import logging
from django.shortcuts import render
from api.serializers import UserRegistrationSerializer, UserLoginSerializer # type: ignore #UserChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth import get_user_model
from .utils import generate_access_token
from django.contrib.auth.decorators import login_required
import jwt 
from api.models import AppUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import check_password


logger = logging.getLogger(__name__)



class EeServiciopaqueteriaListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Serviciopaqueteria.objects.all()
    serializer_class = EeServiciopaqueteriaSerializer

class EeServiciopaqueteriaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Serviciopaqueteria.objects.all()
    serializer_class = EeServiciopaqueteriaSerializer

class PEmpresaListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = P_Empresa.objects.all()
    serializer_class = PEmpresaSerializer

class PEmpresaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = P_Empresa.objects.all()
    serializer_class = PEmpresaSerializer

class AgrCategoriausuarioListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Categoriausuario.objects.all()
    serializer_class = AgrCategoriausuarioSerializer

class AgrCategoriausuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Categoriausuario.objects.all()
    serializer_class = AgrCategoriausuarioSerializer


class AgrUsuarioListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Usuario.objects.all()
    serializer_class = AgrUsuarioSerializer

class AgrUsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Usuario.objects.all()
    serializer_class = AgrUsuarioSerializer

class AgrAlmacenListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Almacen.objects.all()
    serializer_class = AgrAlmacenSerializer
   

class AgrAlmacenRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Almacen.objects.all()
    serializer_class = AgrAlmacenSerializer

class PProveedorListCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = P_Proveedor.objects.all()
    serializer_class = PProveedorSerializer
    def perform_create(self, serializer):
        # Ya no se asigna el usuario autenticado, se toma el usuario del serializador
        serializer.save()


class PProveedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = P_Proveedor.objects.all()
    serializer_class = PProveedorSerializer

class PClientesPListCreate(generics.ListCreateAPIView):
    
    permission_classes = (AllowAny,)
    queryset = P_ClientesP.objects.all()
    serializer_class = PClientesPSerializer
    
    def perform_create(self, serializer):
        provider_id = self.request.data.get('proveedor')
        serializer.save(proveedor_id=provider_id)

class PClientesPRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = P_ClientesP.objects.all()
    serializer_class = PClientesPSerializer

class AgrCategoriaproductoListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Categoriaproducto.objects.all()
    serializer_class = AgrCategoriaproductoSerializer

class AgrCategoriaproductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Categoriaproducto.objects.all()
    serializer_class = AgrCategoriaproductoSerializer

class AgrAlmacenProveedorListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Almacen_Proveedor.objects.all()
    serializer_class = AgrAlmacenProveedorSerializer

class AgrAlmacenProveedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Almacen_Proveedor.objects.all()
    serializer_class = AgrAlmacenProveedorSerializer

class AgrProductosListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Productos.objects.all()
    serializer_class = AgrProductosSerializer

class AgrProductosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Productos.objects.all()
    serializer_class = AgrProductosSerializer

class AgrDetalleproductosListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Detalleproductos.objects.all()
    serializer_class = AgrDetalleproductosSerializer

class AgrDetalleproductosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Detalleproductos.objects.all()
    serializer_class = AgrDetalleproductosSerializer

class AgrFotosListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Fotos.objects.all()
    serializer_class = AgrFotosSerializer

class AgrFotosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Fotos.objects.all()
    serializer_class = AgrFotosSerializer

class AgrCategoriaProductoListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Categoria_Producto.objects.all()
    serializer_class = AgrCategoriaProductoSerializer

class AgrCategoriaProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Categoria_Producto.objects.all()
    serializer_class = AgrCategoriaProductoSerializer

class AgrProductoProveedorListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Producto_Proveedor.objects.all()
    serializer_class = AgrProductoProveedorSerializer

class AgrProductoProveedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Producto_Proveedor.objects.all()
    serializer_class = AgrProductoProveedorSerializer

class AgrSolicitarProductoListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Solicitar_producto.objects.all()
    serializer_class = AgrSolicitarProductoSerializer

class AgrSolicitarProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Solicitar_producto.objects.all()
    serializer_class = AgrSolicitarProductoSerializer

class AgrReporteproductoFallaListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporteproducto_falla.objects.all()
    serializer_class = AgrReporteproductoFallaSerializer

class AgrReporteproductoFallaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporteproducto_falla.objects.all()
    serializer_class = AgrReporteproductoFallaSerializer

class AgrReporteProductoRecibidosListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporte_producto_recibidos.objects.all()
    serializer_class = AgrReporteProductoRecibidosSerializer

class AgrReporteProductoRecibidosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporte_producto_recibidos.objects.all()
    serializer_class = AgrReporteProductoRecibidosSerializer

class EeAlmacenPaqueteriaListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Almacen_Paqueteria.objects.all()
    serializer_class = EeAlmacenPaqueteriaSerializer

class EeAlmacenPaqueteriaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Almacen_Paqueteria.objects.all()
    serializer_class = EeAlmacenPaqueteriaSerializer

class POrdenenvioListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = P_Ordenenvio.objects.all()
    serializer_class = POrdenenvioSerializer

    def perform_create(self, serializer):
        destinatario_id = self.request.data.get('destinatario')
        provider_id = self.request.data.get('proveedor')
        producto_id = self.request.data.get('producto')

        try:
            destinatario = P_ClientesP.objects.get(idclientep=destinatario_id)
            proveedor = P_Proveedor.objects.get(idproveedor=provider_id)
            producto = Agr_Productos.objects.get(idproducto=producto_id)
        except P_ClientesP.DoesNotExist:
            raise ValidationError("Destinatario no encontrado.")
        except P_Proveedor.DoesNotExist:
            raise ValidationError("Proveedor no encontrado.")
        except Agr_Productos.DoesNotExist:
            raise ValidationError("Producto no encontrado.")

        serializer.save(destinatario=destinatario, proveedor=proveedor, producto=producto)

class POrdenenvioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = P_Ordenenvio.objects.all()
    serializer_class = POrdenenvioSerializer

    def update(self, request, *args, **kwargs):
        print("Data received in request.data:", request.data)
        return super().update(request, *args, **kwargs)

class EeRutaListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Ruta.objects.all()
    serializer_class = EeRutaSerializer

class EeRutaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Ruta.objects.all()
    serializer_class = EeRutaSerializer

class EeEnvioListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Envio.objects.all()
    serializer_class = EeEnvioSerializer

class EeEnvioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Envio.objects.all()
    serializer_class = EeEnvioSerializer

class EeEntregaListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Entrega.objects.all()
    serializer_class = EeEntregaSerializer

class EeEntregaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Entrega.objects.all()
    serializer_class = EeEntregaSerializer

class AgrReporteEntregaListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporteentrega.objects.all()
    serializer_class = AgrReporteEntregaSerializer

class AgrReporteEntregaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporteentrega.objects.all()
    serializer_class = AgrReporteEntregaSerializer

class AgrReporteEnvioListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporteenvio.objects.all()
    serializer_class = AgrReporteEnvioSerializer

class AgrReporteEnvioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporteenvio.objects.all()
    serializer_class = AgrReporteEnvioSerializer

class AgrReporteRecoleccionListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporte_Recoleccionp.objects.all()
    serializer_class = AgrReporteRecoleccionSerializer

class AgrReporteRecoleccionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporte_Recoleccionp.objects.all()
    serializer_class = AgrReporteRecoleccionSerializer

class AgrReporteProductoRecibidoListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporte_producto_recibidos.objects.all()
    serializer_class = AgrReporteProductoRecibidosSerializer

class AgrReporteProductoRecibidoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Reporte_producto_recibidos.objects.all()
    serializer_class = AgrReporteProductoRecibidosSerializer

class AgrProductosHistorialListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Productos_historial.objects.all()
    serializer_class = AgrProductosHistorialSerializer

class AgrProductosHistorialRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Agr_Productos_historial.objects.all()
    serializer_class = AgrProductosHistorialSerializer
    
class EeCamionListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Camion.objects.all()
    serializer_class = EeCamionSerializer
    
class EeCamionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Camion.objects.all()
    serializer_class = EeCamionSerializer
    
class EeRepartidorListCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Repartidor.objects.all()
    serializer_class = EeRepartidorSerializer
    
class EeRepartidorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Ee_Repartidor.objects.all()
    serializer_class = EeRepartidorSerializer

class CheckProviderStatusAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny]  # Permitir el acceso sin autenticación

    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer'):
            return Response({'error': 'Authorization header not provided'}, status=400)

        token = auth_header.split(' ')[1]

        try:
            # Decodificar el token JWT
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['idUsuario']
            user = AppUser.objects.get(idUsuario=user_id)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token')
        except AppUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        # Comprobar si el usuario es un proveedor
        is_provider = P_Proveedor.objects.filter(usuario=user).exists()
        return Response({'is_provider': is_provider})
    
class GetProviderIdAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny]

    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer'):
            return Response({'error': 'Authorization header not provided'}, status=400)

        token = auth_header.split(' ')[1]

        try:
            # Decodificar el token JWT
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['idUsuario']
            user = AppUser.objects.get(idUsuario=user_id)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token')
        except AppUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        try:
            provider = P_Proveedor.objects.get(usuario=user)
            return Response({'provider_id': provider.idproveedor})
        except P_Proveedor.DoesNotExist:
            return Response({'error': 'Provider not found'}, status=404)

class GetProviderProductsAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny]

    def get(self, request):
        provider_id = request.query_params.get('provider_id')
        if not provider_id:
            return Response({'error': 'Provider ID not provided'}, status=400)

        try:
            provider = P_Proveedor.objects.get(idproveedor=provider_id)
        except P_Proveedor.DoesNotExist:
            return Response({'error': 'Provider not found'}, status=404)

        # Obtener los productos asociados al proveedor
        products = Agr_Producto_Proveedor.objects.filter(proveedor=provider).select_related('producto')
        product_list = []

        for p in products:
            fotos = Agr_Fotos.objects.filter(producto=p.producto)
            foto_links = [foto.link for foto in fotos]
            
        almacen = p.producto.almacen
        almacen_id = almacen.idalmacen if almacen else None
        almacen = almacen.nombre if almacen else None
            
        product_list.append({
                'id': p.idprodprov,
                'name': p.producto.nombre,
                'stock': p.producto.stock,
                'almacen': almacen,
                'images': foto_links
            })

        return Response({'products': product_list})

class GetProviderClientsAPIView(APIView):
    authentication_classes= (TokenAuthentication,)
    permission_classes = [AllowAny]

    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer'):
            return Response({'error': 'Authorization header not provided'}, status=400)

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['idUsuario']
            user = AppUser.objects.get(idUsuario=user_id)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token')
        except AppUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        try:
            provider = P_Proveedor.objects.get(usuario=user)
        except P_Proveedor.DoesNotExist:
            return Response({'error': 'Provider not found'}, status=404)

        # Obtener los clientes asociados al proveedor
        clients = P_ClientesP.objects.filter(proveedor=provider)
        client_list = [{'id': c.idclientep, 'name': c.nombrepila,'Telefono': c.telefono,'Calle':c.calle} for c in clients]

        return Response({'clients': client_list})


class GetProviderOrdersAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny]

    def get(self, request):
        provider_id = request.query_params.get('provider_id')
        if not provider_id:
            return Response({'error': 'Provider ID not provided'}, status=400)

        try:
            provider = P_Proveedor.objects.get(idproveedor=provider_id)
        except P_Proveedor.DoesNotExist:
            return Response({'error': 'Provider not found'}, status=404)

        # Obtener todas las órdenes y filtrarlas por el proveedor
        orders = P_Ordenenvio.objects.filter(productoproveedor__proveedor=provider).select_related('productoproveedor__producto')
        order_list = []
        for order in orders:
            order_data = {
                'idordenenvio': order.idordenenvio,
                'fecha': order.fecha,
                'cantidad': order.cantidad,
                'destinatario': {
                    'id': order.destinatario.idclientep,
                    'nombre': order.destinatario.nombrepila,
                },
                'producto': {
                    'id': order.productoproveedor.producto.idproducto,
                    'nombre': order.productoproveedor.producto.nombre,
                }
            }
            order_list.append(order_data)

        return Response({'orders': order_list})

##Derian's extra extra stuff


class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            access_token = generate_access_token(new_user)
            response = Response({
                'access_token': access_token,
                'role': new_user.rolUsuario,
                'idUsuario': new_user.idUsuario 
            }, status=status.HTTP_201_CREATED)
            response.set_cookie(key='access_token', value=access_token, httponly=True)
            response.set_cookie(key='user_role', value=new_user.rolUsuario, httponly=True)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            raise AuthenticationFailed('Email and password are required.')

        user = authenticate(username=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials.')

        if user.is_active:
            access_token = generate_access_token(user)
            response = Response({'access_token': access_token, 'role': user.rolUsuario, 'id': user.idUsuario, }, status=status.HTTP_200_OK)
            response.set_cookie(key='access_token', value=access_token, httponly=True)
            response.set_cookie(key='user_role', value=user.rolUsuario, httponly=True)
            response.set_cookie(key='idUsuario', value=user.idUsuario, httponly=True)
            return response

        return Response({'message': 'Something went wrong.'}, status=status.HTTP_400_BAD_REQUEST)

class UserViewAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,) #Aqui tengo un problema, el permiso IsAUthenticated no se cumple, pues al querer agregar esto que significa que solo si el usuario del modelo esta logeado, puede acceder a esta clase. Por ahora no encuentro que sucede, por lo que tendre que dejar el permiso en ALlowAny (no es correcto, pero me sirve para comprobar que el token si esta establecido como cookie)

    def get(self, request):
        token = request.COOKIES.get('access_token')
        if not token:
            raise AuthenticationFailed('Unauthenticated user.')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
           # print(payload)
           # return payload
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated user.')

        user_model = get_user_model()
        user = user_model.objects.filter(idUsuario=payload['idUsuario']).first()
        if not user:
            raise AuthenticationFailed('User not found.')

        serializer = UserRegistrationSerializer(user)
        return Response(serializer.data)

class UserLogoutViewAPI(APIView): 
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,) #Aqui sucede lo mismo, la logica establece que IsAuthenticated nos sirve para ponerle un trozo de seguridad a la api, la cual establece que solo si un usuario esta logeado, puede acceder a esta clase, que sirve para deslogear, sin embargo tampoco sucede esto

    #AUn no se que sucede, debo investigar porque no funciona esa validacion

    def post(self, request):
        response = Response()
        response.delete_cookie('access_token')
        response.data = {'message': 'Logged out successfully.'}
        return response
        
class ChangePasswordView(APIView):
    authentication_classes= (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def post(self, request):
        token = request.headers.get('Authorization')
        if not token:
            return Response({"detail": "Authorization header not provided."}, status=status.HTTP_400_BAD_REQUEST)

        token = token.split(' ')[1]  # Eliminar 'Bearer ' del token

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['idUsuario']
        except jwt.ExpiredSignatureError:
            return Response({"detail": "Token has expired."}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError:
            return Response({"detail": "Invalid token."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = AppUser.objects.get(idUsuario=user_id)
        except AppUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not check_password(serializer.validated_data['old_password'], user.password):
                return Response({"old_password": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"status": "password set"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
class UserChangePasswordView(APIView):
    permission_classes = (AllowAny,) #MIsma situacion con el ISAuthenticated, por cuestiones de avance, lo dejaremos en AllowAny

    def post(self, request, *args, **kwargs):
        serializer = UserChangePasswordSerializer(data=request.data)
        user = request.user

        if serializer.is_valid():
            # Check old password
            if not user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": "Wrong password."}, status=status.HTTP_400_BAD_REQUEST)

            # Set new password
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"detail": "Password has been changed successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''