from django.conf.urls import url
from django.contrib import *
from adi.views import *
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #URL para carga de Template.
    url(r'^menu/$', inicio, name="inicio"),
    url(r'^login_success/$', login_success, name='login_redirect'),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    #DIRECTOR
    url(r'^director/', director, name="director"),
    #ERROR PARA LA INEXISTENCIA DE GRUPOS
    url(r'^error/', login_error, name="errores"),

    url(r'^index_guardia/$', index_guardia, name="index_guardia"),
    url(r'^preceptor/$', preceptor, name="cambio"),
    url(r'^guardia/$', guardia, name="cambio2"),
    url(r'^estadisticas_alumno/$', estadisticas_alumno, name="estadisticas_alumno"),
    url(r'^crearpreceptor/$', cpreceptor, name="cambio4"),
    url(r'^cambiaralumno/$', chalumno, name="cambio6"),

    #URL para pasar ID.
    url(r'^buscar_alumno/(\d+)$', buscar_alumno, name="buscar_alumno"),
    url(r'^crear_fm/(\d+)$', crear_fm, name="crear_fm"),
    url(r'^crear_f1/(\d+)$', crear_f1, name="crear_f1"),
    url(r'^crear_f2/(\d+)$', crear_f2, name="crear_f2"),
    url(r'^crear_f3/(\d+)$', crear_f3, name="crear_f3"),
    url(r'^asistencia/(\d+)$', asistencia, name="asistencia"),
    url(r'^aceptar_formulario/(\d+)$', aceptar_formulario, name="aceptar_formulario"),
    url(r'^rechazar_formulario/(\d+)$', rechazar_formulario, name="rechazar_formulario"),
    url(r'^elegir_formulario/(\d+)$', elegir_formulario, name="elegir_formulario"),
    url(r'^datos_formulario_guardia/(\d+)$', datos_formulario_guardia, name="datos_formulario_guardia"),
    url(r'^datos_formulario_preceptor/(\d+)$', datos_formulario_preceptor, name="datos_formulario_preceptor"),
    url(r'^volver/(\d+)$', volver, name="volver"),

    #URL de funciones sin ID.
    url(r'^crearal/$', crear_alumno, name="crear_alumno"),
    url(r'^mod_alumno/$', mod_alumno, name="mod_alumno"),
    url(r'^crear_preceptor/$', crear_preceptor, name="crear_preceptor"),
    url(r'^busal/$', buscar_alumno, name="buscar_alumno"),
    url(r'^mis_alumnos/$', mis_alumnos, name="mis_alumnos"),

    #URL de cargra de Templates con filtros.
    url(r'^f2/$', f2, name="f2"),
    url(r'^formularios/$', formularios, name="formularios"),
    url(r'^traer_alumnos/$', traer_alumnos, name="traer_alumnos"),
    url(r'^mis_formularios/$', mis_formularios, name="mis_formularios"),
    url(r'^faltas/$', faltas, name="faltas"),
    url(r'^mis_alumnos_presentes/$', mis_alumnos_presentes, name="mis_alumnos_presentes")
]
