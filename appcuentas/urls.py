__author__ = 'williams'

from django.conf.urls import patterns, include, url
from appcuentas import views

urlpatterns = patterns('appcuentas.views',
    url(r'^$', 'view_login'),
    url(r'^login/$', 'view_login'),
)