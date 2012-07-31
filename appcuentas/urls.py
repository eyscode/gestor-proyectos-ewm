__author__ = 'williams'

from django.conf.urls import patterns, include, url
from appcuentas import views

urlpatterns = patterns('appcuentas.views',
    url(r'^$', 'view_login'),
    url(r'^register/$', 'view_register'),
    url(r'^login/$', 'view_login'),
    url(r'^home/$', 'view_home'),
    url(r'^projects/$', 'view_projects'),
    url(r'^account/$', 'view_account'),
    url(r'^groups/$', 'view_groups'),
    url(r'^explore/$', 'view_explore'),
    url(r'^get-client/$', 'view_get_client'),
    url(r'^groups/add-client/$', 'view_groups_add_client'),
    url(r'^projects/add-client/$', 'view_projects_add_client'),
    url(r'^groups/find-client/$', 'view_find_client'),
    url(r'^groups/create-group/$', 'view_create_group'),
    url(r'^projects/create-project/$', 'view_create_project'),
    url(r'^projects/get-project/$', 'view_get_project'),
    url(r'^projects/leave-project/$', 'view_leave_project'),
    url(r'^groups/get-group/$', 'view_get_group'),
    url(r'^groups/delete-group/$', 'view_delete_group'),
    url(r'^projects/delete-project/$', 'view_delete_project'),
    url(r'^projects/tables/$','view_tables'),
    url(r'^projects/reuniones/$','view_reuniones'),
    url(r'^projects/crear_reunion','view_crear_reunion'),
    url(r'^projects/get-boards/$', 'view_get_boards'),
    url(r'^projects/get-board/$', 'view_board'),
    url(r'^projects/create-board/$', 'view_create_board'),
)