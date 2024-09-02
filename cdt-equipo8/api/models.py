from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings

# Create your models here.


class Ee_Serviciopaqueteria(models.Model):
    idpaqueteria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

    class Meta:
        db_table = 'ee_serviciopaqueteria'
    def __str__(self):
        return self.nombre




class P_Empresa(models.Model):
    idempresa = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'p_empresa'

    def __str__(self):
        return self.idempresa



class Agr_Categoriausuario(models.Model):
    idcategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'agr_categoriausuario'

    def __str__(self):
        return self.nombre




## Derian's stuff


# Create your models here.
class AppUserManager(BaseUserManager):
    def create_user(self, email, rolUsuario, password=None,):
        if not email:
            raise ValueError('Email is required.')
        if not password:
            raise ValueError('A password is required.')
        if not rolUsuario:
            raise ValueError('A rolUsuario is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, rolUsuario=rolUsuario)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, rolUsuario, password=None,):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required')
        if not rolUsuario:
            raise ValueError('A rolUsuario is required.')
        user = self.create_user(email,rolUsuario,password,)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user
    
class AppUser(AbstractBaseUser, PermissionsMixin):
    CATEGORY_CHOICES = (
        (1,'Administrador'),
        (2,'Proveedor')
    )
    idUsuario = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    rolUsuario = models.SmallIntegerField(CATEGORY_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['rolUsuario']

    objects= AppUserManager()
    def __str__(self):
        return str(self.idUsuario)
    
    #hay que recordar cambiar el nombre de la tabla dentro de la bd, actualmente no se hace, pero me parece que esta podria ser la solucioon

'''
    class Meta:
        db_table = 'agr_usuario'

'''

##  Cambiar todos las fk de usuario para que agarren la de derian
##  modificar la de appuser para que usen la tabla de categoria_usuario


class Agr_Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=100)
    rolusuario = models.ForeignKey(Agr_Categoriausuario, on_delete=models.CASCADE, db_column='rolusuario')

    class Meta:
        db_table = 'agr_usuario'
    def __str__(self):
        return str(self.idusuario)





class Agr_Almacen(models.Model):
    idalmacen = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=30)
    estatus = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    usuario = models.ForeignKey(AppUser, on_delete=models.CASCADE, db_column='usuario')

    class Meta:
        db_table = 'agr_almacen'
        constraints = [
            models.CheckConstraint(check=models.Q(estatus__in=['Disponible', 'No disponible']), name='estatus_check')
        ]
    def __str__(self):
        return str(self.idalmacen)


class P_Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nombrepila = models.CharField(max_length=50)
    apellidopat = models.CharField(max_length=50)
    apellidomat = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    empresa = models.ForeignKey(P_Empresa, on_delete=models.CASCADE, db_column='empresa')
    usuario = models.ForeignKey(AppUser, on_delete=models.CASCADE, db_column='usuario')

    class Meta:
        db_table = 'p_proveedor'
    def __str__(self):
        return self.nombrepila + ' ' + self.apellidopat + ' ' + self.apellidomat




class P_ClientesP(models.Model):
    idclientep = models.AutoField(primary_key=True)
    nombrepila = models.CharField(max_length=50)
    apellidopat = models.CharField(max_length=50)
    apellidomat = models.CharField(max_length=50)
    codigopostal = models.CharField(max_length=5)
    calle = models.CharField(max_length=50)
    numint = models.CharField(max_length=10)
    numext = models.CharField(max_length=10)
    colonia = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    proveedor = models.ForeignKey(P_Proveedor, on_delete=models.CASCADE, db_column='proveedor')

    class Meta:
        db_table = 'p_clientesp'
    
    def __str__(self):
        return self.nombrepila + ' ' + self.apellidopat + ' ' + self.apellidomat




class Agr_Categoriaproducto(models.Model):
    idcategoriaprod = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'agr_categoriaproducto'
    def __str__(self):
        return self.nombre


class Agr_Almacen_Proveedor(models.Model):
    proveedor = models.ForeignKey(P_Proveedor, on_delete=models.CASCADE, db_column='proveedor')
    almacen = models.ForeignKey(Agr_Almacen, on_delete=models.CASCADE, db_column='almacen')

    class Meta:
        db_table = 'agr_almacen_proveedor'
        unique_together = (('proveedor', 'almacen'),)

    def __str__(self):
        return f"{self.proveedor} - {self.almacen}" 
    
     
    




class Agr_Productos(models.Model):
    idproducto = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=30)
    stock = models.IntegerField()
    almacen = models.ForeignKey(Agr_Almacen, on_delete=models.CASCADE, db_column='almacen')

    class Meta:
        db_table = 'agr_productos'
        constraints = [
            models.CheckConstraint(check=models.Q(stock__gte=0), name='stock_gte_0')
        ]
    def __str__(self):
        return self.idproducto


class Agr_Detalleproductos(models.Model):
    iddetalleproducto = models.AutoField(primary_key=True)
    peso = models.IntegerField()
    estado = models.CharField(max_length=20)
    tamaño = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    producto = models.ForeignKey(Agr_Productos, on_delete=models.CASCADE, db_column='producto')

    class Meta:
        db_table = 'agr_detalleproductos'
        constraints = [
            models.CheckConstraint(check=models.Q(precio__gt=0), name='precio_gt_0')
        ]
    def __str__(self):
        return self.iddetalleproducto


class Agr_Fotos(models.Model):
    idfoto = models.AutoField(primary_key=True)
    link = models.CharField(max_length=200)
    producto = models.ForeignKey(Agr_Productos, on_delete=models.CASCADE, db_column='producto')

    class Meta:
        db_table = 'agr_fotos'
    def __str__(self):
        return self.idfoto



class Agr_Categoria_Producto(models.Model):
    categorias = models.ForeignKey(Agr_Categoriaproducto, on_delete=models.CASCADE, db_column='categorias')
    productos = models.ForeignKey(Agr_Productos, on_delete=models.CASCADE, db_column='productos')

    class Meta:
        db_table = 'agr_categoria_producto'
        unique_together = (('categorias', 'productos'),)



class Agr_Producto_Proveedor(models.Model):
    idprodprov = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(P_Proveedor, on_delete=models.CASCADE, db_column='proveedor', related_name='produto_proveedor1')
    producto = models.ForeignKey(Agr_Productos, on_delete=models.CASCADE, db_column='producto', related_name='produto_proveedor2')

    class Meta:
        db_table = 'agr_producto_proveedor'
        unique_together = (('proveedor', 'producto'),)

    def __str__(self):
        return f'{self.proveedor} - {self.producto}'

    def get_producto(self):
        return self.producto

    




class Agr_Solicitar_producto(models.Model):
    idsolicitud = models.AutoField(primary_key=True)
    almacen = models.ForeignKey(Agr_Almacen, on_delete=models.CASCADE, db_column='almacen')
    proveedor = models.ForeignKey(P_Proveedor, on_delete=models.CASCADE, db_column='proveedor', related_name='solicitar_proveedor')
    producto = models.ForeignKey(Agr_Productos, on_delete=models.CASCADE, db_column='producto', related_name='solicitar_producto')
    cantidad = models.IntegerField()
    fechasol = models.DateField()

    class Meta:
        db_table = 'agr_solicitar_producto'
        constraints = [
            models.CheckConstraint(check=models.Q(cantidad__gt=0), name='cantidad_gt_0')
        ]
    def __str__(self):
        return str(self.idsolicitud)
        


class Agr_Reporteproducto_falla(models.Model):
    idpfallas = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    detalles = models.CharField(max_length=200)
    fecha = models.DateField()
    producto = models.ForeignKey(Agr_Productos, on_delete=models.CASCADE, db_column='producto')

    class Meta:
        db_table = 'agr_reporteproducto_falla'
        constraints = [
            models.CheckConstraint(check=models.Q(cantidad__gte=0), name='cantidad_gte_0')
        ]
    def __str__(self):
        return self.idpfallas



class Agr_Reporte_producto_recibidos(models.Model):
    idprecibidos = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    solicitudpp = models.ForeignKey(Agr_Solicitar_producto, on_delete=models.CASCADE, db_column='solicitudpp')

    class Meta:
        db_table = 'agr_reporte_producto_recibidos'
        constraints = [
            models.CheckConstraint(check=models.Q(cantidad__gte=0), name='cantidad_gte_1')
        ]
    def __str__(self):
        return str(self.idprecibidos)



class Ee_Almacen_Paqueteria(models.Model):
    almacen = models.ForeignKey(Agr_Almacen, on_delete=models.CASCADE, db_column='almacen')
    paqueteria = models.ForeignKey(Ee_Serviciopaqueteria, on_delete=models.CASCADE, db_column='paqueteria')

    class Meta:
        db_table = 'ee_almacen_paqueteria'
        unique_together = (('almacen', 'paqueteria'),)
    def __str__(self):
        return f"{self.almacen} - {self.paqueteria}"


class P_Ordenenvio(models.Model):
    idordenenvio = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    destinatario = models.ForeignKey(P_ClientesP, on_delete=models.CASCADE, db_column='destinatario')
    proveedor = models.ForeignKey(P_Proveedor, on_delete=models.CASCADE, db_column='proveedor', related_name='ordenesenvio_proveedor')
    producto = models.ForeignKey(Agr_Productos, on_delete=models.CASCADE, db_column='producto', related_name='ordenesenvio_producto')

    class Meta:
        db_table = 'p_ordenenvio'
      ##  unique_together = (('producto', 'proveedor'),)
    
    def __str__(self):
        return str(self.idordenenvio)



class Agr_Reporte_Recoleccionp(models.Model):
    idrecoleccionp = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    paqueteria = models.ForeignKey(Ee_Serviciopaqueteria, on_delete=models.CASCADE, db_column='paqueteria')
    ordenenvio = models.ForeignKey(P_Ordenenvio, on_delete=models.CASCADE, db_column='ordenenvio')

    class Meta:
        db_table = 'agr_reporte_recoleccionp'
    def __str__(self):
        return str(self.idrecoleccionp)



class Ee_Envio(models.Model):
    idenvio = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    recoleccion = models.ForeignKey(Agr_Reporte_Recoleccionp, on_delete=models.CASCADE, db_column='recoleccion')

    class Meta:
        db_table = 'ee_envio'
    def __str__(self):
        return str(self.idenvio)


class Ee_Ruta(models.Model):
    idruta = models.AutoField(primary_key=True)
    hora = models.TimeField()
    fecha = models.DateField()
    direccion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    envio = models.ForeignKey(Ee_Envio, on_delete=models.CASCADE, db_column='envio')

    class Meta:
        db_table = 'ee_ruta'
    def __str__(self):
        return self.idruta



class Ee_Entrega(models.Model):
    identrega = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    envio = models.ForeignKey(Ee_Envio, on_delete=models.CASCADE, db_column='envio')

    class Meta:
        db_table = 'ee_entrega'
    def __str__(self):
        return str(self.identrega)



class Agr_Reporteenvio(models.Model):
    idreporteenv = models.AutoField(primary_key=True)
    estatus = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200)
    almacen = models.ForeignKey(Agr_Almacen, on_delete=models.CASCADE, db_column='almacen')
    envio = models.ForeignKey(Ee_Envio, on_delete=models.CASCADE, db_column='envio')
    ordenenvio = models.ForeignKey(P_Ordenenvio, on_delete=models.CASCADE, db_column='ordenenvio')

    class Meta:
        db_table = 'agr_reporteenvio'
        constraints = [
            models.CheckConstraint(check=models.Q(estatus__in=['Entregado', 'Cancelado', 'En camino', 'Con retraso']), name='estatus_check1')
        ]
    def __str__(self):
        return str(self.idreporteenv)



class Agr_Reporteentrega(models.Model):
    idreportent = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    estatus = models.CharField(max_length=15)
    almacen = models.ForeignKey(Agr_Almacen, on_delete=models.CASCADE, db_column='almacen')
    entrega = models.ForeignKey(Ee_Entrega, on_delete=models.CASCADE, db_column='entrega')
    ordenenvio = models.ForeignKey(P_Ordenenvio, on_delete=models.CASCADE, db_column='ordenenvio')

    class Meta:
        db_table = 'agr_reporteentrega'
        constraints = [
            models.CheckConstraint(check=models.Q(estatus__in=['Entregado', 'Cancelado']), name='estatus_check2')
        ]
    def __str__(self):
        return str(self.idreportent)


class Agr_Productos_historial(models.Model):
    idproductoh = models.AutoField(primary_key=True)
    stock = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    estatus = models.CharField(max_length=15)
    producto = models.ForeignKey(Agr_Productos, on_delete=models.CASCADE, db_column='producto')

    class Meta:
        db_table = 'agr_productos_historial'
        constraints = [
            models.CheckConstraint(check=models.Q(estatus__in=['Entrada', 'Salida']), name='estatus_check3')
        ]
    def __str__(self):
        return self.idproductoh

class Ee_Camion(models.Model):
    idcamion = models.AutoField(primary_key=True)
    placas = models.CharField(max_length=7)
    capacidadcarga = models.IntegerField()
    
    class Meta:
        db_table = 'ee_camion'
    
    def __str__(self):
        return str(self.idcamion)

class Ee_Repartidor(models.Model):
    idrepartidor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    camion = models.ForeignKey(Ee_Camion, on_delete=models.CASCADE, db_column='camion')
    paqueteria = models.ForeignKey(Ee_Serviciopaqueteria, on_delete=models.CASCADE, db_column='paqueteria')
    
    class Meta:
        db_table = 'ee_repartidor'
    
    def __str__(self):
        return str(self.idrepartidor)
    
    

