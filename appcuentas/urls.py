__author__ = 'williams'

from django.conf.urls import patterns, include, url
from appcuentas import views

urlpatterns = patterns('appcuentas.views',
    url(r'^$', 'view_login'),
    url(r'^login/$', 'view_login'),
    url(r'^home/$', 'view_home'),
    url(r'^projects/$', 'view_projects'),
    url(r'^account/$', 'view_account'),
    url(r'^groups/$', 'view_groups'),
    url(r'^explore/$', 'view_explore'),
)