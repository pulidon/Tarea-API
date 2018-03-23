from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.utils import timezone

from .models import Tarea

# Create your views here.
def index(request):
	return render(request, 'App/inicio.html')

def tareas_gestion(request):
	tareas_lista = Tarea.objects.order_by('pk')
	context = {'tareas_lista': tareas_lista}
	return render(request, 'App/tarea_gestion.html', context)

def tareas_nueva(request):
	if request.method == 'POST':
		tarea = Tarea()
		tarea.tarea_fecha_de_creacion = timezone.now()
		tarea.tarea_descripcion = request.POST['descripcion']
		tarea.tarea_estado = False
		tarea.tarea_fecha_de_vencimiento = timezone.now()#request.POST['fecha_de_vencimiento']
		tarea.tarea_autor = request.user
		tarea.save()
		return redirect('/App/tareas/gestion')
	else:
		tarea=Tarea()
	context = {'tarea': tarea}
	return render(request, 'App/tarea_nueva.html', context)

def tareas_actualizar(request, pk):
	if request.method == 'POST':
		tarea = get_object_or_404(Tarea, pk=pk)
		tarea.tarea_fecha_de_creacion = timezone.now()
		tarea.tarea_descripcion = request.POST['descripcion']
		tarea.tarea_estado = request.POST['estado']
		tarea.tarea_fecha_de_vencimiento = timezone.now()#request.POST['fecha_de_vencimiento']
		tarea.tarea_autor = request.user
		tarea.save()
		return redirect('/App/tareas/gestion')
	else:
		tarea = get_object_or_404(Tarea, pk=pk)
	context = {'tarea': tarea}
	return render(request, 'App/tarea_actualizar.html', context)

def tareas_borrar(request, pk):
	if request.method == 'POST':
		tarea = Tarea.objects.get(pk=pk)
		tarea.delete()
		return redirect('/App/tareas/gestion')
	else:
		tarea = get_object_or_404(Tarea, pk=pk)
		context = {'tarea': tarea}
	return render(request, 'App/tarea_borrar.html', context)

def tareas_consultar(request):
	tareas_lista = Tarea.Objects.order_by('fecha_creacion')#Agregar los diferentes parametros de busqueda
	context = {'tareas_lista': tareas_lista}
	return render(request, 'App/tarea_consultar.html', context)