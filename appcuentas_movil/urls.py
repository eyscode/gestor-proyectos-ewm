__author__ = 'williams'

from django.conf.urls import patterns, include, url
from appcuentas import views

urlpatterns = patterns('appcuentas_movil.views',
    url(r'^app/login$', 'view_login_movil'),
    url(r'^app/proyectos$', 'view_traer_proyectos_movil'),
    url(r'^app/tableros', 'view_traer_tableros_movil'),
    url(r'^app/columnas', 'view_traer_columnas_movil'),
    url(r'^app/tareas_columna', 'view_traer_tareas_columna_movil'),
)