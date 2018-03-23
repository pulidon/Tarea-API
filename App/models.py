from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarea(models.Model):
	tarea_fecha_de_creacion = models.DateTimeField('fecha creacion')
	tarea_descripcion = models.TextField('descripcion')
	tarea_estado = models.BooleanField('finalizada')
	tarea_fecha_de_vencimiento = models.DateTimeField('fecha vencimiento')
	tarea_autor = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.tarea_descripcion
