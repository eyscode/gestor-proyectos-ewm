# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.utils import simplejson
from oauth2 import clients
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
    grupos = Group.objects.filter(creador=Client.objects.get(user=request.user)).order_by('-date_creation')
    clients = Client.objects.exclude(user=request.user)
    return render_to_response("desktop/groups.html",
            {'ext': ext, 'actual': 'groups', 'grupos': grupos, 'clients': clients},
        context_instance=RequestContext(request))


def view_find_client(request):
    clients = Client.objects.exclude(id=request.user.id)
    return render_to_response("desktop/contenido-buscar.html",
            {'clients': clients}, context_instance=RequestContext(request))


def view_create_group(request):
    try:
        error = {'nombre': [], 'descripcion': []}
        if request.method == "POST":
            if request.POST.get('nombre') and request.POST.get('descripcion'):
                nombre = request.POST.get('nombre')
                descripcion = request.POST.get('descripcion')
                if not Group.objects.filter(creador=request.user.get_profile(), name=nombre):
                    Group.objects.create(name=nombre, information=descripcion, creador=request.user.get_profile())
                    return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
                else:
                    error['nombre'].append('Ya existe un grupo con ese nombre')
            elif request.POST.get('nombre') and not request.POST.get('descripcion'):
                nombre = request.POST.get('nombre')
                if Group.objects.filter(creador=request.user.get_profile(), name=nombre):
                    error['nombre'].append('Ya existe un grupo con ese nombre')
                error['descripcion'].append('Debe ingresar una descripcion')
            elif request.POST.get('descripcion') and not request.POST.get('nombre'):
                error['nombre'].append('Debe ingresar un nombre')
            elif not request.POST.get('descripcion') and not request.POST.get('nombre'):
                error['descripcion'].append('Debe ingresar una descripcion')
                error['nombre'].append('Debe ingresar un nombre')
            return HttpResponse(simplejson.dumps({'estado': 0, 'error': error}), mimetype='application/json')
        else:
            return render_to_response("desktop/create-group.html", context_instance=RequestContext(request))
    except Exception, ex:
        print ex
        return HttpResponse(simplejson.dumps({'estado': 0, 'error': 'No se pudo crear el grupo'}),
            mimetype='application/json')


def view_delete_group(request):
    try:
        if 'groupid' in request.GET:
            group = get_object_or_404(Group, id=request.GET.get('groupid'))
            group.delete()
            return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
    except Exception, ex:
        print ex
        return HttpResponse(simplejson.dumps({'estado': 0}), mimetype='application/json')


def view_get_group(request):
    try:
        error = {'nombre': [], 'descripcion': []}
        if request.method == "POST":
            if request.POST.get('nombre') and request.POST.get('descripcion'):
                nombre = request.POST.get('nombre')
                descripcion = request.POST.get('descripcion')
                mi_grupo = Group.objects.get(creador=request.user.get_profile(), id=request.POST.get('groupid'))
                existeotro = Group.objects.filter(creador=request.user.get_profile(), name=nombre).exclude(
                    id=request.POST.get('groupid'))
                if existeotro:
                    print "va a salir un error"
                    error['nombre'].append('Ya existe un grupo con ese nombre')
                elif mi_grupo:
                    mi_grupo.name = nombre
                    mi_grupo.information = descripcion
                    mi_grupo.save()
                    users = request.POST.get('users')
                    groups = Group_has_Client.objects.filter(group__id=request.POST.get('groupid'))
                    for ghc in groups:
                        ghc.delete()
                    if users:
                        users = users.split(',')
                        for userid in users:
                            Group_has_Client.objects.create(group=Group.objects.get(id=request.POST.get('groupid')),
                                client=Client.objects.get(user__id=userid))
                    return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
                else:
                    return HttpResponse(simplejson.dumps({'estado': 2, 'error': 'No se pudo editar'}),
                        mimetype='application/json')
            elif request.POST.get('nombre') and not request.POST.get('descripcion'):
                nombre = request.POST.get('nombre')
                if Group.objects.filter(creador=request.user.get_profile(), name=nombre):
                    error['nombre'].append('Ya existe un grupo con ese nombre')
                error['descripcion'].append('Debe ingresar una descripcion')
            elif request.POST.get('descripcion') and not request.POST.get('nombre'):
                error['nombre'].append('Debe ingresar un nombre')
            elif not request.POST.get('descripcion') and not request.POST.get('nombre'):
                error['descripcion'].append('Debe ingresar una descripcion')
                error['nombre'].append('Debe ingresar un nombre')
            return HttpResponse(simplejson.dumps({'estado': 0, 'error': error}), mimetype='application/json')
        else:
            group = Group.objects.get(id=request.GET.get('idgroup'))
            groups = Group_has_Client.objects.filter(group__id=request.GET.get('idgroup'))
            clients = []
            for ghc in groups:
                clients.append(ghc.client)
            return render_to_response("desktop/get-group.html", {'clients': clients, 'group': group},
                context_instance=RequestContext(request))
    except Exception, ex:
        print ex
        return HttpResponse(simplejson.dumps({'estado': 2, 'error': 'No se pudo editar'}),
            mimetype='application/json')


def view_get_client(request):
    if 'name' in request.GET and request.GET.get('name'):
        try:
            client = request.GET.get('name')
            clients_nombre = User.objects.filter(first_name__icontains=client).exclude(id=request.user.id)
            clients_apellidos = User.objects.filter(last_name__icontains=client).exclude(id=request.user.id)
            clients = set(clients_nombre).union(set(clients_apellidos))
        except Exception, ex:
            clients = User.objects.exclude(id=request.user.id)
    else:
        clients = User.objects.exclude(id=request.user.id)
    clients = serializers.serialize('json', clients)
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