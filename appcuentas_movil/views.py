# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail.message import EmailMultiAlternatives
from django.http import HttpResponse, Http404
from django.utils import simplejson
from appcuentas.models import Project, Table, Column

def view_login_movil(request):
    try:
        to_json = None
        if request.is_ajax() and request.method == "POST":
            username = request.POST.get("email", "")
            password = request.POST.get("password", "")
            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    to_json = {
                        "id": request.user.id
                    }
                    return HttpResponse(simplejson.dumps(to_json), content_type="text/plain")
            to_json = {
                "id": -1
            }
            return HttpResponse(simplejson.dumps(to_json), content_type="text/plain")
        raise Http404
    except Exception, ex:
        print ex
        raise Http404


def view_password_movil(request):
    to_json = None
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
    raise 404


@login_required(login_url='/login/')
def view_traer_proyectos_movil(request):
    to_json = None
    if request.is_ajax() and request.method == "POST":
        id_user = request.POST.get("id_user", -1)
        if id_user == -1:
            proyectos = None
            to_json = {
                "proyectos": proyectos
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
        else:
            proyectos = Project.objects.filter(client__user__id=id_user)
            to_json = {
                "proyectos": proyectos
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    raise 404


@login_required(login_url='/login/')
def view_traer_tableros_movil(request):
    to_json = None
    if request.is_ajax() and request.method == "GET":
        id_proyecto = request.GET.get("id_proyecto", -1)
        if id_proyecto == -1:
            tableros = None
            to_json = {
                "tableros": tableros
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
        else:
            tableros = Table.objects.filter(project__id=id_proyecto)
            to_json = {
                "tableros": tableros
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    raise 404


@login_required(login_url='/login/')
def view_datos_tableros_movil(request):
    to_json = None
    if request.is_ajax() and request.method == "GET":
        id_tablero = request.GET.get("id_tablero", -1)
        if id_tablero == -1:
            tableros = None
            to_json = {
                "tableros": tableros
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
        else:
            #falta hacer la correccion de la consulta
            tableros = None
            to_json = {
                "tableros": tableros
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    raise 404


@login_required(login_url='/login/')
def view_datos_columnas_movil(request):
    to_json = None
    if request.is_ajax() and request.method == "GET":
        id_tablero = request.GET.get("id_tablero", -1)
        if id_tablero == -1:
            columnas = None
            to_json = {
                "columnas": columnas
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
        else:
            #falta hacer la correccion de la consulta
            columnas = Column.objects.filter(table__id=id_tablero)
            to_json = {
                "columnas": columnas
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    raise 404