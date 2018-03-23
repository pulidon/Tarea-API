from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Tarea

# Create your tests here.
class TareasAPITests(TestCase):
	def test_no_hay_tareas(self):
		response = self.client.get(reverse('App:tareas_gestion'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No hay tareas que mostrar")

	def test_crear_tarea(self):
		response = self.client.get(reverse('App:tareas_nueva'))
		self.assertEqual(response.status_code, 200)
	
	def test_actualizar_tarea(self):
		response = self.client.get(reverse('App:tareas_actualizar'))
		self.assertEqual(response.status_code, 200)	

	def test_borrar_tarea(self):
		response = self.client.get(reverse('App:tareas_actualizar'))
		self.assertEqual(response.status_code, 200)	
