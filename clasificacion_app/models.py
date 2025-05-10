# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    liga = models.ForeignKey('Liga', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        managed = False
        db_table = 'equipo'


class Jornada(models.Model):
    id = models.AutoField(primary_key=True)
    liga = models.ForeignKey('Liga', models.DO_NOTHING, blank=True, null=True)
    numero = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.numero}"

    class Meta:
        managed = False
        db_table = 'jornada'


class Jugador(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    dorsal = models.IntegerField()
    posicion = models.CharField(max_length=10, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    id_equipo = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='id_equipo', blank=True, null=True)
    goles = models.IntegerField(blank=True, null=True)
    tarjetas_amarillas = models.IntegerField(blank=True, null=True)
    tarjetas_rojas = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.primer_apellido}"

    class Meta:
        managed = False
        db_table = 'jugador'


class Liga(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        managed = False
        db_table = 'liga'


class Partido(models.Model):
    id = models.AutoField(primary_key=True)
    liga = models.ForeignKey(Liga, models.DO_NOTHING, blank=True, null=True)
    jornada = models.ForeignKey(Jornada, models.DO_NOTHING, blank=True, null=True)
    equipo_local = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='equipo_local', blank=True, null=True)
    equipo_visitante = models.ForeignKey(Equipo, models.DO_NOTHING, db_column='equipo_visitante', related_name='partido_equipo_visitante_set', blank=True, null=True)
    arbitro = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    estadio = models.CharField(max_length=100, blank=True, null=True)
    goles_local = models.IntegerField(blank=True, null=True)
    goles_visitante = models.IntegerField(blank=True, null=True)
    tarjetas_amarillas_local = models.IntegerField(blank=True, null=True)
    tarjetas_rojas_local = models.IntegerField(blank=True, null=True)
    tarjetas_amarillas_visitantes = models.IntegerField(blank=True, null=True)
    tarjetas_rojas_visitante = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipo_local}  - {self.equipo_visitante}"

    class Meta:
        managed = False
        db_table = 'partido'
