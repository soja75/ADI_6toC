# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser, User, Group
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import *
from .redirect import *
from .decorators import *
from django.contrib.auth.decorators import login_required, user_passes_test

def crear_fm(request, dni_alumno):
    return HttpResponse("Funca")

def crear_f1(request, dni_alumno):
    return HttpResponse("Funca")

def crear_f2(request, dni_alumno):
    #Tomamos al usuario loggueado
    pepe = request.user
    #Buscamos al alumno a partir del Dni
    alumno2 = Alumno.objects.get(dni=dni_alumno)
    prec = Preceptor.objects.get(nombre_usuario=pepe)
    if alumno2.estado=="Saliendo":
        return render(request, 'preceptor/usuario_con_form.html')
    else:
        #Modificamos el estado del alumno, para que este no aparezaca en usuarios disponibles para Formulario
        #alumno2.estado="Saliendo"
        #alumno2.save()
        ahorita = timezone.now()
        #Creamos el Formulario de tipo True ya que es un F2
        new_f = Formulario(alumno=alumno2, fecha=ahorita, estado="Proceso", preceptor=prec, tipo="True")
        new_f.save()
    return HttpResponse("Hecho")

def datos_formulario_preceptor(request, id_for):
    print id_for;
    formi = Formulario.objects.get(id=id_for)
    alum = formi.alumno
    if formi.tipo == True:
        print "Es un F2"
        return render(request,
                  'preceptor/formularios/datos_f2.html',
                  {'forms2':formi})
    if formi.tipo == False:
        print "Es un F3"
        return render(request,
                  'preceptor/formularios/datos_f3.html',
                  {'forms3':formi})

def crear_f3(request, dni_alumno):
    #Tomamos al usuario loggueado
    pepe = request.user
    #Buscamos al alumno a partir del Dni
    alumno2 = Alumno.objects.get(dni=dni_alumno)
    prec = Preceptor.objects.get(nombre_usuario=pepe)
    if alumno2.estado=="Saliendo":
        return render(request, 'preceptor/usuario_con_form.html')
    else:
        #Modificamos el estado del alumno, para que este no aparezaca en usuarios disponibles para Formulario
        #alumno2.estado="Saliendo"
        #alumno2.save()
        ahorita = timezone.now()
        #Creamos el Formulario de tipo False ya que es un F3
        new_f = Formulario(alumno=alumno2, fecha=ahorita, estado="Proceso", preceptor=prec, tipo="False")
        new_f.save()
    return HttpResponse('FUNCIONO')

def buscar_alumno(request, dni_alumno):
    global al
    al = Alumno.objects.get(dni=dni_alumno)
    return render(request, 'admin/modificar_alumno.html', {'alumno':al})

def mod_alumno(request):
    nombre2 = request.POST['nombre']
    apellido2 = request.POST['apellido']
    al.nombre=nombre2
    al.apellido=apellido2
    al.save()
    print al.apellido
    data = {
        'estado': al.apellido + " actualizado"
    }
    return JsonResponse(data, safe=False)

def estadisticas_alumno(request):
    cant_presente = 0
    cant_ausentes = 0
    cant_saliendo = 0
    pepe = request.user
    prec = Preceptor.objects.get(nombre_usuario=pepe)
    cant_presente = Curso.objects.filter(alumno__estado="Presente", preceptor=prec).count()
    cant_ausentes = Curso.objects.filter(alumno__estado="Ausente", preceptor=prec).count()
    cant_saliendo = Curso.objects.filter(alumno__estado="Saliendo", preceptor=prec).count()
    data = {
        'presente': cant_presente,
        'ausente': cant_ausentes,
        'saliendo': cant_saliendo
    }
    return JsonResponse(data)

def crear_alumno(request):
    if request.method=="POST":
        nombre = request.POST['nombre_alumno']
        apellido = request.POST['apellido_alumno']
        dni = request.POST['dni_alumno']
        legajo = request.POST['legajo_alumno']
        fecha_de_nacimiento = request.POST['fecha_nacimiento_alumno']
        direccion = request.POST['direccion_alumno']
        #foto = request.POST['foto_alumno']
        #tutor = request.POST['tutor_alumno']
        curso = Curso.objects.get(pk=1)
        tutor = Tutor.objects.get(nombre="Pepito")
        #print curso
        g = Group.objects.get(name='Alumno')
        grupo_usuario = g
        aux = request.user
        alumno = Alumno(nombre=nombre, apellido=apellido, dni=dni, legajo=legajo, direccion=direccion, curso=curso, tutor=tutor, nombre_usuario=aux, grupo_usuario=grupo_usuario)
        alumno.save()
        print alumno
    return HttpResponse('FUNCIONO')


def crear_preceptor(request):
    if request.method == 'POST':
        print "llega"
        nombre_usuario = request.POST['nombre_usuario']
        password = request.POST['password']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        dni = request.POST['dni']
        #Creamos al modelo Preceptor a partir de los datos ingresados, relacionando nombre_usuario con el User creado
        preceptor = Preceptor(nombre_usuario=nombre_usuario,nombre=nombre, apellido=apellido, dni=dni)
        preceptor.save()
        #Creamos al usuario
        user = User.objects.create_user(username=nombre_usuario, password=password, email="asdfaas@preceptor.com")
        user.save()
    return render(request, 'inicio.html')

def aceptar_formulario(request, alum_t):
    formulario = Formulario.objects.get(id=alum_t)
    nom = formulario.alumno.nombre
    al = Alumno.objects.get(nombre=nom)
    if al:
        al.estado="Presente"
        al.save()
        formulario.estado="Finalizado"
        formulario.save()
        data = {
            'estado': al.nombre + " aceptado",
        }
    else:
        data = {
            'estado':"La operación falló"
        }
    print al.padre.email
    print "llegamos2"
    return JsonResponse(data, safe=False)

def rechazar_formulario(request, alum_t):
    formulario = Formulario.objects.get(id=alum_t)
    nom = formulario.alumno.nombre
    al = Alumno.objects.get(nombre=nom)
    if al:
        #al.estado="Indefinido"
        #al.save()
        formulario.estado="Rechazado"
        formulario.save()
        data = {
            'estado': al.nombre + " RECHAZADO",
        }
    else:
        data = {
            'estado':"La operación falló"
        }
    return JsonResponse(data, safe=False)

def asistencia(request, alum_id):
    al = Alumno.objectos.get(dni=alum_id)
    if al.estado == "Ausente":
        al.estado = "Presente"
        al.save()
        data = {
            'estado': al.apellido + " Presente "
        }
    if al.estado == "Presente":
        al.estado = "Ausente"
        al.save()
        data = {
            'estado': al.apellido + " Ausente "
        }
    return JsonResponse(data, safe=False)

def volver(request, alum_t):
    al = Alumno.objects.filter(dni=alum_t)
    if request.method == 'POST':
        al.update(estado="Presente")
    return HttpResponse('FUNCIONO')

def elegir_formulario(request, id_for):
    al = Alumno.objects.get(id=id_for)
    print "aca estoy"
    return render (request, 'preceptor/formularios/elegir_formulario.html', {'alumno':al})

def datos_formulario_guardia(request, id_for):
    print id_for;
    formi = Formulario.objects.get(id=id_for)
    alum = formi.alumno
    return render(request,
                  'guardia/datos.html',
                  {'form':formi})

def f2(request):
    pepe = request.user
    try:
        prec = Preceptor.objects.get(nombre_usuario=pepe)
        al = Alumno.objects.filter(curso=prec.curso, estado="Presente").order_by('-apellido')
    except:
        al = None
    return render(request,
                 'preceptor/formularios/elegir_formulario.html',
                 {'todos_los_alumnos':al})

def formularios(request):
    try:
        forms2 = Formulario.objects.filter(tipo="True", estado="Proceso")
        forms3 = Formulario.objects.filter(tipo="False", estado="Proceso")
    except:
        forms2 = None
        forms3 = None
    print forms2
    print forms3
    return render(request,'guardia/formularios.html',{'todos_los_f3':forms3, 'todos_los_f2':forms2})

def mis_alumnos_presentes(request):
    pepe = request.user
    prec = Preceptor.objects.get(nombre_usuario=pepe)
    al = Alumno.objects.filter(curso__preceptor=prec, estado="ND")
    return HttpResponse (al)
    #return render(request, 'preceptor/formularios/elegir_formulario.html', {'todos_los_alumnos': al})

def mis_alumnos(request):
    pepe = request.user
    prec = Preceptor.objects.get(nombre_usuario=pepe)
    al = Alumno.objects.filter(curso__preceptor=prec).order_by('curso__division', 'apellido', 'nombre')
    return render(request,
                 'preceptor/alumnos/mis_alumnos.html',
                 {'todos_los_alumnos':al})

def faltas(request):
    pepe = request.user
    prec = Preceptor.objects.get(nombre_usuario=pepe)
    al = Alumno.objects.filter(curso__preceptor=prec).order_by('curso__division', 'apellido', 'nombre')
    return render(request,
                 'preceptor/alumnos/faltas.html',
                 {'todos_los_alumnos':al})

def traer_alumnos(request):
    al = Alumno.objects.all()
    return render(request,'admin/buscar_alumno.html',{'todos_los_alumnos':al})

def mis_formularios(request):
    pepe = request.user
    prec = Preceptor.objects.get(nombre_usuario=pepe)
    try:
        forms2 = Formulario.objects.filter(tipo="True", estado="Proceso", preceptor=prec)
        forms3 = Formulario.objects.filter(tipo="False", estado="Proceso", preceptor=prec)
    except:
        forms2 = None
        forms3 = None
    return render(request,'preceptor/formularios/mis_formularios.html',{'todos_los_f3':forms3, 'todos_los_f2':forms2})

#Renderizar este template si al loguearse no se encuentra el usuario en un grupo.
def login_error(request):
    return render(request, 'login_errores.html')

#FALTA PREVENIR LOGINS DE OTROSS USUARIOS A LOGINS UNICOS DE OTROS USUARIOS
def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="Preceptor").exists():
        # Si el usuario pertenece al grupo de Preceptor, LOGIN_REDIRECT_URL va a actuar sobre la url 'cambio.'
        return redirect("cambio")

    if request.user.groups.filter(name="Director").exists():
        # Si el usuario pertenece al grupo de Director, LOGIN_REDIRECT_URL va a actuar sobre la url 'director'
        return redirect("director")
    else:
        return redirect('errores')
    """
    if request.user.groups.filter(name="Alumno_o_Tutor").exists():
        # Si el usuario pertenece al grupo de Alumno_o_Tutor, LOGIN_REDIRECT_URL va a actuar sobre la url 'alumnos_y_tutores'
        return redirect("alumnos_y_tutores")

    if request.user.groups.filter(name="Guardia").exists():
        # Si el usuario pertenece al grupo de Guardia, LOGIN_REDIRECT_URL va a actuar sobre la url 'guardia'
        return redirect("guardia")
    """
