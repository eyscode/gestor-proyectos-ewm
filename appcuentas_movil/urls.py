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
    url(r'^app/ver_plantilla', 'view_traer_plantillas'),
    url(r'^app/crear_proyecto', 'view_crear_proyecto'),
    url(r'^app/eliminar_proyecto', 'view_eliminar_proyecto'),
    url(r'^app/agregar_paquete_tablero', 'view_agregar_paquete_tablero'),
    url(r'^app/agregar_tarea_columna','view_agregar_tarea_columna'),
    url(r'^app/detalles_tarea','view_detalles_tarea'),
    url(r'^app/add_miembro_projecto','view_add_miembros_proyecto'),
    url(r'^app/add_comentario','view_agregar_comentario_tarea'),
    url(r'^app/mover_tarea','view_mover_tarea'),
    url(r'^app/add_miembro_grupo','view_add_miembros_grupo'),
    url(r'^app/add_grupo','view_add_grupo'),
    url(r'^app/reuniones','view_traer_reuniones'),
    url(r'^app/comentarios','view_traer_comentarios'),
    url(r'^app/profile','view_traer_profile'),
)