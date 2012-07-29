# Create your views here.
#import json
import datetime
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
    try:
        if request.method == "GET":
            id_proyecto = request.GET.get("id_proyecto", -1)
            callback = request.GET.get('callback', '')
            print id_proyecto
            if id_proyecto == -1:
                response = callback + '([]);'
                return HttpResponse(response, mimetype='application/json')
            else:
                paquetes = Work_Package.objects.filter(project__id= id_proyecto )
                response = serializers.serialize("json",paquetes)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
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
    try:
        if request.method == "GET":
            id_paquete = request.GET.get("id_paquete", -1)
            callback = request.GET.get('callback', '')
            if id_paquete == -1:
                response = callback + '([]);'
                return HttpResponse(response, mimetype='application/json')
            else:
                tareas =Task.objects.filter(work_package__id= id_paquete )
                response = serializers.serialize("json",tareas)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404

@login_required(login_url='/login/')
def view_crear_tablero(request):
    try:
        if request.method == "GET":
            nombre_tablero = request.GET.get("nombre_tablero", -1)
            id_project = request.GET.get("id_projecto", -1)
            callback = request.GET.get('callback', '')
            print nombre_tablero
            print id_project
            req={}
            if nombre_tablero!=-1 and id_project!=-1:
                p= get_object_or_404(Project,id=id_project)
                print p.name
                table = Table(name=nombre_tablero,date_creation=datetime.datetime.now(),columns=0,project=p)
                table.save()

                req['id']= 1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
            else:
                req['id']= -1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404

@login_required(login_url='/login/')
def view_crear_columna(request):
    try:
        if request.method == "GET":
            nombre_columna = request.GET.get("nombre_columna", -1)
            id_tablero = request.GET.get("id_tablero", -1)
            callback = request.GET.get('callback', '')
            print nombre_columna
            print id_tablero
            req={}
            if nombre_columna!=-1 and id_tablero!=-1:
                t= get_object_or_404(Table,id=id_tablero)
                num=t.columns+1
                colum = Column(name=nombre_columna,position=num,table=t)
                colum.save()
                t.columns=num
                t.save()
                req['id']= 1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
            else:
                req['id']= -1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404

@login_required(login_url='/login/')
def view_edit_columnas(request):
    try:
        if request.method == "GET":
            id_tablero = request.GET.get("id_tablero", -1)
            id_columna =request.GET.get("id_columna", -1)
            posicion = request.GET.get("posicion", -1)
            nombre_column = request.GET.get("nombre_columna", -1)
            callback = request.GET.get('callback', '')
            print nombre_tablero
            print id_project
            req={}
            if  id_tablero!=-1:
                columna = get_object_or_404(Column,id=id_columna)
                columnas = Column.objects.filter(table__id=id_tablero)
                if posicion!=-1:
                    posi_actual=columna.position
                    if posi_actual<posicion:
                        for c in columnas:
                            if posi_actual < c.position <= posicion:
                                c.position=c.position-1
                                c.save()
                    else:
                        for c in columnas:
                            if posi_actual>c.position >= posicion:
                                c.position=c.position+1
                                c.save()
                    columna.position=posicion
                if nombre_column!=-1:
                    columna.name=nombre_column
                columna.save()
                req['id']= 1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
            else:
                req['id']= -1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404


@login_required(login_url='/login/')
def view_datos_edit_columna(request):
    try:
        if request.method == "GET":
            id_columna = request.GET.get("id_columna", -1)
            id_tablero =request.GET.get("id_tablero", -1)
            callback = request.GET.get('callback', '')
            print nombre_tablero
            print id_project
            req={}
            if id_columna!=-1 :
                columna= get_object_or_404(Column,id=id_columna)
                tablero = get_object_or_404(Table,id=id_tablero)
                req['id']= 1
                req['name']=columna.name
                req['num']=tablero.columns
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
            else:
                req['id']= -1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404

@login_required(login_url='/login/')
def view_crear_paquete(request):
    try:
        if request.method == "GET":
            nombre_paquete = request.GET.get("nombre", -1)
            descripcion_paquete = request.GET.get("descripcion", -1)
            prioridad_paquete = request.GET.get("prioridad", -1)
            id_project = request.GET.get("id_projecto", -1)
            callback = request.GET.get('callback', '')
            req={}
            if nombre_paquete!=-1 and id_project!=-1 and descripcion_paquete!=-1 and prioridad_paquete!=-1:
                p= get_object_or_404(Project,id=id_project)
                pack = Work_Package(description=descripcion_paquete,name=nombre_paquete,prioridad=prioridad_paquete,project=p)
                pack.save()
                req['id']= 1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
            else:
                req['id']= -1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404

@login_required(login_url='/login/')
def view_crear_tarea(request):
    try:
        if request.method == "GET":
            titulo = request.GET.get("titulo", -1)
            subtitulo = request.GET.get("subtitulo", -1)
            descripcion = request.GET.get("descripcion", -1)
            id_paquete = request.GET.get("id_paquete", -1)
            callback = request.GET.get('callback', '')
            req={}
            print titulo
            print descripcion
            print id_paquete
            if titulo!=-1 and descripcion!=-1 and id_paquete!=-1:
                p= get_object_or_404(Work_Package,id=id_paquete)
                print p.name
                task = Task(title=titulo,subtitle=subtitulo,description=descripcion,state='',work_package=p)
                task.save()
                req['id']= 1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
            else:
                req['id']= -1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404

def view_traer_plantillas(request):
    try:
        projects=Project.objects.filter(template= True )
        response = serializers.serialize("json", projects)
        response = callback + '(' + response + ');'
        return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404

@login_required(login_url='/login/')
def view_crear_project(request):
    try:
        if request.method == "GET":
            nombre = request.GET.get("nombre", -1)
            compania = request.GET.get("compania", -1)
            template = request.GET.get("id_template", -1)
            id_user = request.GET.get("id_usuario", -1)
            callback = request.GET.get('callback', '')
            req={}
            print titulo
            print descripcion
            print id_paquete
            if nombre!=-1 and id_user!=-1:
                c=get_object_or_404(Client,user__id=id_user)
                project = Project(name=nombre,data_creation=datetime.datetime.now(),company=compania, template=False , creador=c)
                project.save()
                if template!=-1 or template!='':
                    pt=get_object_or_404(Project,id=template)
                    pt_tableros= Table.objects.filter(project=pt)
                    for pt in pt_tableros:
                        table_project=Table(name=pt.name,date_creation=datetime.datetime.now(),columns=pt.columns,project=project)
                        table_project.save()
                        colum=Column.objects.filter(table=pt)
                        for pt_co in colum:
                            co_porject=Column(name=pt_co.name,position=pt_co.position,table=table_project)
                            co_porject.save()
                req['id']= 1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
            else:
                req['id']= -1
                response = simplejson.dumps(req)
                response = callback + '(' + response + ');'
                return HttpResponse(response, mimetype='application/json')
    except Exception, ex:
        print ex
    raise Http404