from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class EeServiciopaqueteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ee_Serviciopaqueteria
        fields = '__all__'

class PEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = P_Empresa
        fields = '__all__'

class AgrCategoriausuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Categoriausuario
        fields = '__all__'

class AgrUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Usuario
        fields = '__all__'

class AgrAlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Almacen
        fields = '__all__'

class PProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = P_Proveedor
        fields = '__all__'

class PClientesPSerializer(serializers.ModelSerializer):
    class Meta:
        model = P_ClientesP
        fields = '__all__'

class AgrCategoriaproductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Categoriaproducto
        fields = '__all__'

class AgrAlmacenProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Almacen_Proveedor
        fields = '__all__'

class AgrProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Productos
        fields = '__all__'

class AgrDetalleproductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Detalleproductos
        fields = '__all__'

class AgrFotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Fotos
        fields = '__all__'

class AgrCategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Categoria_Producto
        fields = '__all__'

class AgrProductoProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Producto_Proveedor
        fields = '__all__'

class AgrSolicitarProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Solicitar_producto
        fields = '__all__'

class AgrReporteproductoFallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Reporteproducto_falla
        fields = '__all__'

class AgrReporteProductoRecibidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Reporte_producto_recibidos
        fields = '__all__'

class EeAlmacenPaqueteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ee_Almacen_Paqueteria
        fields = '__all__'

class POrdenenvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = P_Ordenenvio
        fields = '__all__'

class EeRutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ee_Ruta
        fields = '__all__'

class EeEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ee_Envio
        fields = '__all__'

class EeEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ee_Entrega
        fields = '__all__'

class AgrReporteEntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Reporteentrega
        fields = '__all__'

class AgrReporteEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Reporteenvio
        fields = '__all__'

class AgrReporteRecoleccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Reporte_Recoleccionp
        fields = '__all__'

class AgrProductosHistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agr_Productos_historial
        fields = '__all__'

class EeCamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ee_Camion
        fields = '__all__'
        
class EeRepartidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ee_Repartidor
        fields = '__all__'




##Derian's extra stuff

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
    rolUsuario = serializers.ChoiceField(choices=[
        (1, 'Administrador'),
        (2, 'Proveedor')
    ])

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'rolUsuario']

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        rolUsuario = validated_data.get('rolUsuario')

        if rolUsuario == 1:  # Administrador
            user = self.Meta.model.objects.create_superuser(email=email, rolUsuario=rolUsuario, password=password)
        elif rolUsuario == 2:  # Proveedor
            user = self.Meta.model.objects.create_user(email=email, rolUsuario=rolUsuario, password=password)
        else:
            raise ValueError('Invalid rolUsuario')

        return user
    
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError("New passwords do not match")
        return data