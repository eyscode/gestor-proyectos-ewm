# Create your views here.
#import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.mail.message import EmailMultiAlternatives
##from django.core.serializers import json
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils import simplejson
from appcuentas.models import Project, Table, Column, Work_Package, Task, Client, Client_has_Project

"""
    para jsonp
    req = {}
    req ['username'] = username
    req ['password'] = password
    response = simplejson.dumps(req)
    response = callback + '(' + response + ');'
    return HttpResponse(response, mimetype="application/json")
"""

def view_login_movil(request):
    try:
        req = {}
        callback = request.GET.get('callback', '')
        username = request.GET.get("email", "")
        password = request.GET.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                req['id']= request.user.id
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
            req['id']= -1
            response = simplejson.dumps(req)
            response = callback + '(' + response + ');'
            return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
        raise Http404


def view_password_movil(request):
    to_json ={}
    if request.is_ajax() and request.method == "GET":
        email = request.GET.get("email", "")
        if email and User.objects.filter(email=email):
            subject = "recuperar contrasenia"
            from_email = "acm.unmsm@gmail.com"
            to = email
            text_content = " "
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            #msg.attach_alternative(html_content, "text/html")
            msg.send()
            to_json = {
                "result": True
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
        else:
            to_json = {
                "result": False
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    raise Http404


@login_required(login_url='/login/')
def view_traer_proyectos_movil(request):
    id_user = request.GET.get("id_user", -1)
    callback = request.GET.get('callback', '')
    print id_user
    try:
        if id_user == -1:
            proyectos = None
            to_json['proyectos'] = proyectos
            response = simplejson.dumps(to_json)
            response = callback + '(' + response + ');'
            return HttpResponse(response, mimetype='application/json')
        else:
            #client=get_object_or_404(Client,user__id=id_user)
            proyectos1 = Client_has_Project.objects.filter(client__user__id=id_user)
            proyectos2=Project.objects.filter(creador__user__id=id_user)
            proyectos=set(proyectos1).union(set(proyectos2))
            response = serializers.serialize("json", proyectos)
            response = callback + '(' + response + ');'
            return HttpResponse(response, mimetype='application/json')
    except Exception,ex:
        print ex
    raise Http404

@login_required(login_url='/login/')
def view_traer_grupos_movil(request):
    to_json = {}
    id_user = request.GET.get("id_user", -1)
    callback = request.GET.get('callback', '')
    if id_user == -1:
        groups = None
        to_json['grupos'] = groups
        response = simplejson.dumps(to_json)
        response = callback + '(' + response + ');'
        return HttpResponse(response, mimetype='application/json')
    else:
        groups = Project.objects.filter(client__user__id=id_user)
        to_json['grupos'] = groups
        response = simplejsorn.dumps(to_json)
        response = callback + '(' + response + ');'
        return HttpResponse(response, mimetype='application/json')
    raise Http404

@login_required(login_url='/login/')
def view_traer_tableros_movil(request):
    try:
        if request.method == "GET":
            id_proyecto = request.GET.get("id_proyecto", -1)
            callback = request.GET.get('callback', '')
            print id_proyecto
            if id_proyecto == -1:
                response = callback + '([]);'
                return HttpResponse(response, mimetype='application/json')
            else:
                tableros = Table.objects.filter(project__id= id_proyecto )
                response = serializers.serialize("json",tableros)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404

@login_required(login_url='/login/')
def view_traer_columnas_movil(request):
    try:
        if request.method == "GET":
            id_tablero = request.GET.get("id_tablero", -1)
            callback = request.GET.get('callback', '')
            print id_tablero
            if id_tablero == -1:
                response = callback + '([]);'
                return HttpResponse(response, mimetype='application/json')
            else:
                columnas = Column.objects.filter(table__id=id_tablero)
                response = serializers.serialize("json",columnas)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404

@login_required(login_url='/login/')
def view_traer_paquetes_movil(request):
    to_json = {}
    if request.method == "GET":
        id_proyecto = request.GET.get("id_proyecto", -1)
        callback = request.GET.get('callback', '')
        if id_proyecto == -1:
            paquetes = None
            to_json['paquetes'] = paquetes
            response = simplejson.dumps(to_json)
            response = callback + '(' + response + ');'
            return HttpResponse(response, mimetype='application/json')
        else:
            paquetes = Work_Package.objects.filter(project__id= id_proyecto )
            to_json['paquetes'] = paquetes
            response = simplejson.dumps(to_json)
            response = callback + '(' + response + ');'
            return HttpResponse(response, mimetype='application/json')
    raise Http404

@login_required(login_url='/login/')
def view_traer_tareas_columna_movil(request):
    try:
        if request.method == "GET":
            id_columna = request.GET.get("id_columna", -1)
            callback = request.GET.get('callback', '')
            if id_columna == -1:
                response = callback + '([]);'
                return HttpResponse(response, mimetype='application/json')
            else:
                tareas =Task.objects.filter(column__id= id_columna )
                response = serializers.serialize("json",tareas)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404



@login_required(login_url='/login/')
def view_traer_tareas_pack_movil(request):
    to_json = {}
    if request.method == "GET":
        id_paquete = request.GET.get("id_paquete", -1)
        callback = request.GET.get('callback', '')
        if id_proyecto == -1:
            tareas = None
            to_json['tareas'] = tareas
            response = simplejson.dumps(to_json)
            response = callback + '(' + response + ');'
            return HttpResponse(response, mimetype='application/json')
        else:
            tareas = Task.objects.filter(task_packete__id= id_paquete )
            to_json['tareas'] = tareas
            response = simplejson.dumps(to_json)
            response = callback + '(' + response + ');'
            return HttpResponse(response, mimetype='application/json')
    raise Http404

