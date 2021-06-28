from django.db import models

# Create your models here.

class projet (models.Model):
    id_proj = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=999, blank=False)
    descrpcion= models.TextField(max_length=600, blank=True)
    estado= models.BooleanField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_fin= models.DateTimeField(auto_now=False, default=0)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    tipo_aplicacion= models.CharField(max_length=10, blank=True)
    modalidad= models.CharField(max_length=25, blank=True)
    sector = models.CharField(max_length=15, blank=True)
    cobertura_proyecto = models.CharField(max_length=40, blank=True)
    linea_investigacion= models.CharField(max_length=25, blank=True)
    sublinea_invest= models.CharField(max_length=50, blank=True)
    linea_especifica= models.CharField(max_length=20, blank=True)
    objetivo_general= models.TextField(max_length=999, blank=True)
    objetivos_especificos= models.TextField(max_length=200, blank=True)
    presupuesto=models.DecimalField(max_digits=15, decimal_places=2, default=0)
    id_user = models.ForeignKey('usuarios',
                                on_delete=models.CASCADE, db_column='id_user')
    id_inst = models.ForeignKey('instituciones',
                                on_delete=models.CASCADE, db_column='id_inst')
    class Meta:
        db_table = 'projet'
        verbose_name = 'proyectos'

    def __str__(self):
        return self.titulo

class usuarios (models.Model):
    id_user= models.AutoField(primary_key=True)
    Nombre = models. CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    email= models.CharField(max_length=50, blank=True)
    class Meta:
        db_table= 'usuarios'
        verbose_name= 'users'
    def __str__(self):
        return self.Nombre



class instituciones (models.Model):
    id_inst= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, verbose_name='NOMBRES')
    repre = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=500, blank=True)
    contact= models.CharField(max_length=20, blank=True)
    convenio = models.BooleanField(default=1)


    class Meta:
        db_table='instituciones'
        verbose_name= 'institute'

    def __str__(self):
        return self.nombre


