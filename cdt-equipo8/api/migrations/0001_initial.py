# Generated by Django 5.0.7 on 2024-09-05 02:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agr_Categoriaproducto',
            fields=[
                ('idcategoriaprod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'agr_categoriaproducto',
            },
        ),
        migrations.CreateModel(
            name='Agr_Categoriausuario',
            fields=[
                ('idcategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'agr_categoriausuario',
            },
        ),
        migrations.CreateModel(
            name='Agr_Reporte_Recoleccionp',
            fields=[
                ('idrecoleccionp', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'db_table': 'agr_reporte_recoleccionp',
            },
        ),
        migrations.CreateModel(
            name='Ee_Camion',
            fields=[
                ('idcamion', models.AutoField(primary_key=True, serialize=False)),
                ('placas', models.CharField(max_length=7)),
                ('capacidadcarga', models.IntegerField()),
            ],
            options={
                'db_table': 'ee_camion',
            },
        ),
        migrations.CreateModel(
            name='Ee_Serviciopaqueteria',
            fields=[
                ('idpaqueteria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'ee_serviciopaqueteria',
            },
        ),
        migrations.CreateModel(
            name='P_ClientesP',
            fields=[
                ('idclientep', models.AutoField(primary_key=True, serialize=False)),
                ('nombrepila', models.CharField(max_length=50)),
                ('apellidopat', models.CharField(max_length=50)),
                ('apellidomat', models.CharField(max_length=50)),
                ('codigopostal', models.CharField(max_length=5)),
                ('calle', models.CharField(max_length=50)),
                ('numint', models.CharField(max_length=10)),
                ('numext', models.CharField(max_length=10)),
                ('colonia', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'p_clientesp',
            },
        ),
        migrations.CreateModel(
            name='P_Empresa',
            fields=[
                ('idempresa', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'p_empresa',
            },
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('rolUsuario', models.SmallIntegerField(verbose_name=((1, 'Administrador'), (2, 'Proveedor')))),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Agr_Almacen',
            fields=[
                ('idalmacen', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('estatus', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('usuario', models.ForeignKey(db_column='usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'agr_almacen',
            },
        ),
        migrations.CreateModel(
            name='Agr_Productos',
            fields=[
                ('idproducto', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('stock', models.IntegerField()),
                ('almacen', models.ForeignKey(db_column='almacen', on_delete=django.db.models.deletion.CASCADE, to='api.agr_almacen')),
            ],
            options={
                'db_table': 'agr_productos',
            },
        ),
        migrations.CreateModel(
            name='Agr_Fotos',
            fields=[
                ('idfoto', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=200)),
                ('producto', models.ForeignKey(db_column='producto', on_delete=django.db.models.deletion.CASCADE, to='api.agr_productos')),
            ],
            options={
                'db_table': 'agr_fotos',
            },
        ),
        migrations.CreateModel(
            name='Agr_Detalleproductos',
            fields=[
                ('iddetalleproducto', models.AutoField(primary_key=True, serialize=False)),
                ('peso', models.IntegerField()),
                ('estado', models.CharField(max_length=20)),
                ('tamaño', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('producto', models.ForeignKey(db_column='producto', on_delete=django.db.models.deletion.CASCADE, to='api.agr_productos')),
            ],
            options={
                'db_table': 'agr_detalleproductos',
            },
        ),
        migrations.CreateModel(
            name='Agr_Categoria_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorias', models.ForeignKey(db_column='categorias', on_delete=django.db.models.deletion.CASCADE, to='api.agr_categoriaproducto')),
                ('productos', models.ForeignKey(db_column='productos', on_delete=django.db.models.deletion.CASCADE, to='api.agr_productos')),
            ],
            options={
                'db_table': 'agr_categoria_producto',
            },
        ),
        migrations.CreateModel(
            name='Agr_Productos_historial',
            fields=[
                ('idproductoh', models.AutoField(primary_key=True, serialize=False)),
                ('stock', models.IntegerField()),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('estatus', models.CharField(max_length=15)),
                ('producto', models.ForeignKey(db_column='producto', on_delete=django.db.models.deletion.CASCADE, to='api.agr_productos')),
            ],
            options={
                'db_table': 'agr_productos_historial',
            },
        ),
        migrations.CreateModel(
            name='Agr_Reporteproducto_falla',
            fields=[
                ('idpfallas', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('detalles', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('producto', models.ForeignKey(db_column='producto', on_delete=django.db.models.deletion.CASCADE, to='api.agr_productos')),
            ],
            options={
                'db_table': 'agr_reporteproducto_falla',
            },
        ),
        migrations.CreateModel(
            name='Agr_Solicitar_producto',
            fields=[
                ('idsolicitud', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('fechasol', models.DateField()),
                ('almacen', models.ForeignKey(db_column='almacen', on_delete=django.db.models.deletion.CASCADE, to='api.agr_almacen')),
                ('producto', models.ForeignKey(db_column='producto', on_delete=django.db.models.deletion.CASCADE, related_name='solicitar_producto', to='api.agr_productos')),
            ],
            options={
                'db_table': 'agr_solicitar_producto',
            },
        ),
        migrations.CreateModel(
            name='Agr_Reporte_producto_recibidos',
            fields=[
                ('idprecibidos', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('solicitudpp', models.ForeignKey(db_column='solicitudpp', on_delete=django.db.models.deletion.CASCADE, to='api.agr_solicitar_producto')),
            ],
            options={
                'db_table': 'agr_reporte_producto_recibidos',
            },
        ),
        migrations.CreateModel(
            name='Agr_Usuario',
            fields=[
                ('idusuario', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=50, unique=True)),
                ('contraseña', models.CharField(max_length=100)),
                ('rolusuario', models.ForeignKey(db_column='rolusuario', on_delete=django.db.models.deletion.CASCADE, to='api.agr_categoriausuario')),
            ],
            options={
                'db_table': 'agr_usuario',
            },
        ),
        migrations.CreateModel(
            name='Ee_Envio',
            fields=[
                ('idenvio', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('recoleccion', models.ForeignKey(db_column='recoleccion', on_delete=django.db.models.deletion.CASCADE, to='api.agr_reporte_recoleccionp')),
            ],
            options={
                'db_table': 'ee_envio',
            },
        ),
        migrations.CreateModel(
            name='Ee_Entrega',
            fields=[
                ('identrega', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('envio', models.ForeignKey(db_column='envio', on_delete=django.db.models.deletion.CASCADE, to='api.ee_envio')),
            ],
            options={
                'db_table': 'ee_entrega',
            },
        ),
        migrations.CreateModel(
            name='Ee_Ruta',
            fields=[
                ('idruta', models.AutoField(primary_key=True, serialize=False)),
                ('hora', models.TimeField()),
                ('fecha', models.DateField()),
                ('direccion', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('envio', models.ForeignKey(db_column='envio', on_delete=django.db.models.deletion.CASCADE, to='api.ee_envio')),
            ],
            options={
                'db_table': 'ee_ruta',
            },
        ),
        migrations.CreateModel(
            name='Ee_Repartidor',
            fields=[
                ('idrepartidor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('camion', models.ForeignKey(db_column='camion', on_delete=django.db.models.deletion.CASCADE, to='api.ee_camion')),
                ('paqueteria', models.ForeignKey(db_column='paqueteria', on_delete=django.db.models.deletion.CASCADE, to='api.ee_serviciopaqueteria')),
            ],
            options={
                'db_table': 'ee_repartidor',
            },
        ),
        migrations.CreateModel(
            name='Ee_Almacen_Paqueteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('almacen', models.ForeignKey(db_column='almacen', on_delete=django.db.models.deletion.CASCADE, to='api.agr_almacen')),
                ('paqueteria', models.ForeignKey(db_column='paqueteria', on_delete=django.db.models.deletion.CASCADE, to='api.ee_serviciopaqueteria')),
            ],
            options={
                'db_table': 'ee_almacen_paqueteria',
            },
        ),
        migrations.AddField(
            model_name='agr_reporte_recoleccionp',
            name='paqueteria',
            field=models.ForeignKey(db_column='paqueteria', on_delete=django.db.models.deletion.CASCADE, to='api.ee_serviciopaqueteria'),
        ),
        migrations.CreateModel(
            name='P_Ordenenvio',
            fields=[
                ('idordenenvio', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('destinatario', models.ForeignKey(db_column='destinatario', on_delete=django.db.models.deletion.CASCADE, to='api.p_clientesp')),
                ('producto', models.ForeignKey(db_column='producto', on_delete=django.db.models.deletion.CASCADE, related_name='ordenesenvio_producto', to='api.agr_productos')),
            ],
            options={
                'db_table': 'p_ordenenvio',
            },
        ),
        migrations.CreateModel(
            name='Agr_Reporteenvio',
            fields=[
                ('idreporteenv', models.AutoField(primary_key=True, serialize=False)),
                ('estatus', models.CharField(max_length=15)),
                ('descripcion', models.CharField(max_length=200)),
                ('almacen', models.ForeignKey(db_column='almacen', on_delete=django.db.models.deletion.CASCADE, to='api.agr_almacen')),
                ('envio', models.ForeignKey(db_column='envio', on_delete=django.db.models.deletion.CASCADE, to='api.ee_envio')),
                ('ordenenvio', models.ForeignKey(db_column='ordenenvio', on_delete=django.db.models.deletion.CASCADE, to='api.p_ordenenvio')),
            ],
            options={
                'db_table': 'agr_reporteenvio',
            },
        ),
        migrations.CreateModel(
            name='Agr_Reporteentrega',
            fields=[
                ('idreportent', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('estatus', models.CharField(max_length=15)),
                ('almacen', models.ForeignKey(db_column='almacen', on_delete=django.db.models.deletion.CASCADE, to='api.agr_almacen')),
                ('entrega', models.ForeignKey(db_column='entrega', on_delete=django.db.models.deletion.CASCADE, to='api.ee_entrega')),
                ('ordenenvio', models.ForeignKey(db_column='ordenenvio', on_delete=django.db.models.deletion.CASCADE, to='api.p_ordenenvio')),
            ],
            options={
                'db_table': 'agr_reporteentrega',
            },
        ),
        migrations.AddField(
            model_name='agr_reporte_recoleccionp',
            name='ordenenvio',
            field=models.ForeignKey(db_column='ordenenvio', on_delete=django.db.models.deletion.CASCADE, to='api.p_ordenenvio'),
        ),
        migrations.CreateModel(
            name='P_Proveedor',
            fields=[
                ('idproveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombrepila', models.CharField(max_length=50)),
                ('apellidopat', models.CharField(max_length=50)),
                ('apellidomat', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('empresa', models.ForeignKey(db_column='empresa', on_delete=django.db.models.deletion.CASCADE, to='api.p_empresa')),
                ('usuario', models.ForeignKey(db_column='usuario', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'p_proveedor',
            },
        ),
        migrations.AddField(
            model_name='p_ordenenvio',
            name='proveedor',
            field=models.ForeignKey(db_column='proveedor', on_delete=django.db.models.deletion.CASCADE, related_name='ordenesenvio_proveedor', to='api.p_proveedor'),
        ),
        migrations.AddField(
            model_name='p_clientesp',
            name='proveedor',
            field=models.ForeignKey(db_column='proveedor', on_delete=django.db.models.deletion.CASCADE, to='api.p_proveedor'),
        ),
        migrations.AddField(
            model_name='agr_solicitar_producto',
            name='proveedor',
            field=models.ForeignKey(db_column='proveedor', on_delete=django.db.models.deletion.CASCADE, related_name='solicitar_proveedor', to='api.p_proveedor'),
        ),
        migrations.CreateModel(
            name='Agr_Producto_Proveedor',
            fields=[
                ('idprodprov', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.ForeignKey(db_column='producto', on_delete=django.db.models.deletion.CASCADE, related_name='produto_proveedor2', to='api.agr_productos')),
                ('proveedor', models.ForeignKey(db_column='proveedor', on_delete=django.db.models.deletion.CASCADE, related_name='produto_proveedor1', to='api.p_proveedor')),
            ],
            options={
                'db_table': 'agr_producto_proveedor',
            },
        ),
        migrations.CreateModel(
            name='Agr_Almacen_Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('almacen', models.ForeignKey(db_column='almacen', on_delete=django.db.models.deletion.CASCADE, to='api.agr_almacen')),
                ('proveedor', models.ForeignKey(db_column='proveedor', on_delete=django.db.models.deletion.CASCADE, to='api.p_proveedor')),
            ],
            options={
                'db_table': 'agr_almacen_proveedor',
            },
        ),
        migrations.AddConstraint(
            model_name='agr_almacen',
            constraint=models.CheckConstraint(check=models.Q(('estatus__in', ['Disponible', 'No disponible'])), name='estatus_check'),
        ),
        migrations.AddConstraint(
            model_name='agr_productos',
            constraint=models.CheckConstraint(check=models.Q(('stock__gte', 0)), name='stock_gte_0'),
        ),
        migrations.AddConstraint(
            model_name='agr_detalleproductos',
            constraint=models.CheckConstraint(check=models.Q(('precio__gt', 0)), name='precio_gt_0'),
        ),
        migrations.AlterUniqueTogether(
            name='agr_categoria_producto',
            unique_together={('categorias', 'productos')},
        ),
        migrations.AddConstraint(
            model_name='agr_productos_historial',
            constraint=models.CheckConstraint(check=models.Q(('estatus__in', ['Entrada', 'Salida'])), name='estatus_check3'),
        ),
        migrations.AddConstraint(
            model_name='agr_reporteproducto_falla',
            constraint=models.CheckConstraint(check=models.Q(('cantidad__gte', 0)), name='cantidad_gte_0'),
        ),
        migrations.AddConstraint(
            model_name='agr_reporte_producto_recibidos',
            constraint=models.CheckConstraint(check=models.Q(('cantidad__gte', 0)), name='cantidad_gte_1'),
        ),
        migrations.AlterUniqueTogether(
            name='ee_almacen_paqueteria',
            unique_together={('almacen', 'paqueteria')},
        ),
        migrations.AddConstraint(
            model_name='agr_reporteenvio',
            constraint=models.CheckConstraint(check=models.Q(('estatus__in', ['Entregado', 'Cancelado', 'En camino', 'Con retraso'])), name='estatus_check1'),
        ),
        migrations.AddConstraint(
            model_name='agr_reporteentrega',
            constraint=models.CheckConstraint(check=models.Q(('estatus__in', ['Entregado', 'Cancelado'])), name='estatus_check2'),
        ),
        migrations.AddConstraint(
            model_name='agr_solicitar_producto',
            constraint=models.CheckConstraint(check=models.Q(('cantidad__gt', 0)), name='cantidad_gt_0'),
        ),
        migrations.AlterUniqueTogether(
            name='agr_producto_proveedor',
            unique_together={('proveedor', 'producto')},
        ),
        migrations.AlterUniqueTogether(
            name='agr_almacen_proveedor',
            unique_together={('proveedor', 'almacen')},
        ),
    ]
