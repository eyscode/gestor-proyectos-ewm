# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.utils import simplejson
from appcuentas.models import Group, Group_has_Client
from models import Client, User
from forms import RegisterForm
from django.core import serializers

def view_login(request):
    error = None
    if request.method == "POST":
        usuario = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if usuario and password:
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return redirect(to="/home")
            else:
                error = "Su password o usuario es incorrecto"
    return render_to_response("desktop/inicio.html", {"error": error}, context_instance=RequestContext(request))


def view_register(request):
    registerform = RegisterForm()
    if request.POST:
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            nombre = registerform.cleaned_data["nombre"]
            apellidos = registerform.cleaned_data["apellidos"]
            email = registerform.cleaned_data["email"]
            perfil = registerform.cleaned_data["perfil"]
            passw = registerform.cleaned_data["password"]
            repassw = registerform.cleaned_data["repassw"]
            u = User.objects.create(nombre, apellidos, email)
            Client.objects.create(user=u, profile=perfil)
            return redirect(to="/board")
    return render_to_response("desktop/register.html", {"rf": registerform}, context_instance=RequestContext(request))


@login_required(login_url='/login/')
def view_home(request):
    if request.is_ajax():
        ext = "desktop/vacio.html"
    else:
        ext = "desktop/layout.html"
    print ext
    return render_to_response("desktop/home.html", {'ext': ext, 'actual': 'home'},
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def view_projects(request):
    if request.is_ajax():
        ext = "desktop/vacio.html"
    else:
        ext = "desktop/layout.html"
    return render_to_response("desktop/projects.html", {'ext': ext, 'actual': 'projects'},
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def view_groups(request):
    if request.is_ajax():
        ext = "desktop/vacio.html"
    else:
        ext = "desktop/layout.html"
    grupos = Group_has_Client.objects.filter(client=Client.objects.get(user=request.user))
    return render_to_response("desktop/groups.html", {'ext': ext, 'actual': 'groups', 'grupos': grupos},
        context_instance=RequestContext(request))


def view_get_client(request):
    if 'name' in request.GET and request.GET.get('name'):
        try:
            client = request.GET.get('name')
            clients_nombre = User.objects.filter(first_name__icontains=client)
            clients_apellidos = User.objects.filter(last_name__icontains=client)
            clients = set(clients_nombre).union(set(clients_apellidos))
            clients = serializers.serialize('json', clients)
        except Exception, ex:
            clients = []
    else:
        clients = []
    return HttpResponse(clients, mimetype="application/json")


def view_add_client(request):
    if 'iduser' in request.GET and 'idgroup' in request.GET and request.GET.get('name'):
        try:
            client = request.GET.get('iduser')
            clients_apellidos = User.objects.filter(last_name__icontains=client)
            clients = set(clients_nombre).union(set(clients_apellidos))
            clients = serializers.serialize('json', clients)
        except Exception, ex:
            clients = []
    else:
        clients = []
    return HttpResponse(clients, mimetype="application/json")


@login_required(login_url='/login/')
def view_account(request):
    if request.is_ajax():
        ext = "desktop/vacio.html"
    else:
        ext = "desktop/layout.html"
    return render_to_response("desktop/account.html", {'ext': ext, 'actual': 'account'},
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def view_explore(request):
    if request.is_ajax():
        ext = "desktop/vacio.html"
    else:
        ext = "desktop/layout.html"
    return render_to_response("desktop/explore.html", {'ext': ext, 'actual': 'explore'},
        context_instance=RequestContext(request))


@login_required(login_url="/login")
def view_board(request):
    return render_to_response("board.html", context_instance=RequestContext(request))