__author__ = ''

from django.conf.urls import patterns, include, url
from appcuentas import views

urlpatterns = patterns('appcuentas_movil.views',
    url(r'^app/login$', 'view_login_movil'),
    url(r'^app/proyectos$', 'view_traer_proyectos_movil'),
    url(r'^app/tableros', 'view_traer_tableros_movil'),
    url(r'^app/columnas', 'view_traer_columnas_movil'),
    url(r'^app/tareas_columna', 'view_traer_tareas_columna_movil'),
    url(r'^app/paquetes', 'view_traer_paquetes_movil'),
    url(r'^app/tareas_paquete', 'view_traer_tareas_pack_movil'),
    url(r'^app/crear_tablero', 'view_crear_tablero'),
    url(r'^app/crear_columna', 'view_crear_columna'),
    url(r'^app/crear_paquete', 'view_crear_paquete'),
    url(r'^app/crear_tarea', 'view_crear_tarea'),
)