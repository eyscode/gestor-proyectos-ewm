# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils import simplejson
from appcuentas.models import Group, Group_has_Client, Project
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
    grupos = Group.objects.filter(creador=Client.objects.get(user=request.user))
    #clients = Client.objects.exclude(user=request.user)
    clients = Client.objects.all()
    return render_to_response("desktop/groups.html",
            {'ext': ext, 'actual': 'groups', 'grupos': grupos, 'clients': clients},
        context_instance=RequestContext(request))


def view_find_client(request):
    clients = Client.objects.all()
    return render_to_response("desktop/contenido-buscar.html",
            {'clients': clients}, context_instance=RequestContext(request))


def view_create_group(request):
    try:
        error = {'nombre': [], 'descripcion': []}
        if request.method == "POST":
            if request.POST.get('nombre') and request.POST.get('descripcion'):
                nombre = request.POST.get('nombre')
                descripcion = request.POST.get('descripcion')
                if not Group.objects.filter(creador=request.user.get_profile(), nombre=nombre):
                    Group.objects.create(name=nombre, information=descripcion, creador=request.user.get_profile())
                    return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
                else:
                    error['nombre'].append('Ya existe un grupo con ese nombre')
            elif request.POST.get('nombre') and not request.POST.get('descripcion'):
                error['descripcion'].append('Debe ingresar una descripcion')
            elif request.POST.get('description') and not request.POST.get('nombre'):
                error['nombre'].append('Debe ingresar un nombre')
            elif not request.POST.get('description') and not request.POST.get('nombre'):
                error['descripcion'].append('Debe ingresar una descripcion')
                error['nombre'].append('Debe ingresar un nombre')
            return HttpResponse(simplejson.dumps({'estado': 0, 'error': error}), mimetype='application/json')
        else:
            return render_to_response("desktop/create-group.html", context_instance=RequestContext(request))
    except Exception, ex:
        print ex


def view_get_client(request):
    if 'name' in request.GET and request.GET.get('name'):
        try:
            client = request.GET.get('name')
            clients_nombre = User.objects.filter(first_name__icontains=client)
            clients_apellidos = User.objects.filter(last_name__icontains=client)
            clients = set(clients_nombre).union(set(clients_apellidos))
            clients = serializers.serialize('json', clients)
        except Exception, ex:
            clients = User.objects.all()
    else:
        clients = User.objects.all()
    return HttpResponse(clients, mimetype="application/json")


def view_add_client(request):
    if 'iduser' in request.GET and 'idgroup' in request.GET and request.GET.get('iduser') and request.GET.get(
        'idgroup'):
        try:
            client = get_object_or_404(User, id=request.GET.get('iduser'))
            client = get_object_or_404(Client, user=client)
            group = get_object_or_404(Group, id=request.GET.get('idgroup'))
            existe = Group_has_Client.objects.filter(client=client, group=group)
            if not existe:
                Group_has_Client.objects.create(client=client, group=group)
                return HttpResponse(1, mimetype="application/json")
            else:
                return HttpResponse(2, mimetype="application/json")
        except Exception, ex:
            print ex
    else:
        pass
    return HttpResponse(0, mimetype="application/json")


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