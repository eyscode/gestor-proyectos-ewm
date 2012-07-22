# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail.message import EmailMultiAlternatives
from django.http import HttpResponse
from django.utils import simplejson
from appcuentas.models import Project

def view_login_movil(request):
    to_json = None
    if request.is_ajax() and request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        if username and password:
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                to_json={
                    "id": request.user.id
                }
                HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
        to_json={
            "id": -1
        }
        return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    raise 404

def view_password_movil(request):
    to_json = None
    if request.is_ajax() and request.method == "GET":
        email = request.GET.get("email","")
        if email and User.objects.filter(email=email):
            subject = "recuperar contraseña"
            from_email = "acm.unmsm@gmail.com"
            to = email
            text_content = " "
            #msg.attach_alternative(html_content, "text/html")
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            to_json={
                "result": True
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
        else:
            to_json={
                "result": False
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    raise 404

@login_required(login_url='/login/')
def view_traer_proyectos(request):
    to_json = None
    if request.is_ajax() and request.method == "GET":
        id_user = request.POST.get("id_user",-1)
        if id_user == -1:
            proyectos = None
            to_json={
                "proyectos": proyectos
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
        else:
            proyectos = Project.objects.filter(client__user__id=id_user)
            to_json={
                "proyectos": proyectos
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    raise 404