from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

# -------------------- ESTUDIANTES --------------------

def index(request):
    """
    Listar los registros del modelo Estudiante.
    """
    estudiantes = Estudiante.objects.all()
    informacion_template = {
        'estudiantes': estudiantes,
        'numero_estudiantes': len(estudiantes)
    }
    return render(request, 'index.html', informacion_template)

def obtener_estudiante(request, id):
    estudiante = Estudiante.objects.get(pk=id)
    return render(request, 'obtener_estudiante.html', {'estudiante': estudiante})

def crear_estudiante(request):
    if request.method == 'POST':
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EstudianteForm()
    return render(request, 'crearEstudiante.html', {'formulario': formulario})

def editar_estudiante(request, id):
    estudiante = Estudiante.objects.get(pk=id)
    if request.method == 'POST':
        formulario = EstudianteForm(request.POST, instance=estudiante)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EstudianteForm(instance=estudiante)
    return render(request, 'editarEstudiante.html', {'formulario': formulario})

def eliminar_estudiante(request, id):
    estudiante = Estudiante.objects.get(pk=id)
    estudiante.delete()
    return redirect(index)

# -------------------- PAISES --------------------

def crear_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_paises')
    else:
        form = PaisForm()
    return render(request, 'crear_pais.html', {'form': form})

def ver_paises(request):
    paises = Pais.objects.all()
    return render(request, 'ver_paises.html', {'paises': paises})
