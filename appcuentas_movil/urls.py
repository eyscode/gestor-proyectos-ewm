__author__ = 'williams'

from django.conf.urls import patterns, include, url
from appcuentas import views

urlpatterns = patterns('appcuentas_movil.views',
    url(r'^app/login$', 'view_login_movil'),
)