__author__ = 'Romell'

from django.conf.urls import patterns, url, include

urlpatterns = patterns('app_romell.views',
    url(r'^app_romell/$','create_reunion'),
    url(r'^app_romell/create_group/$','create_reunion'),
    url(r'^app_romell/upload/$','upload_file'),
)