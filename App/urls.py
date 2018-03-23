from django.urls import path

from . import views

app_name = 'App'
urlpatterns = [
	path('', views.index, name='index'),
	path('tareas/gestion', views.tareas_gestion, name='tareas_gestion'),
	path('tareas/nueva', views.tareas_nueva, name='tareas_nueva'),
	path('tareas/actualizar/<int:pk>', views.tareas_actualizar, name='tareas_actualizar'),
	path('tareas/borrar/<int:pk>', views.tareas_borrar, name='tareas_borrar'),
	path('tareas/consultar', views.tareas_consultar, name='tareas_consultar'),
]