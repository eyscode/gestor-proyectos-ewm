__author__ = 'Romell'

from django.conf.urls import patterns, url

urlpatterns = patterns('app_romell.views',
    url(r'^app_romell/$','create_group'),
    url(r'^app_romell/create_group/$','create_group'),
    url(r'^app_romell/upload/$','upload_file'),
)