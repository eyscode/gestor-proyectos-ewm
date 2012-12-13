# Create your views here.
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.utils import simplejson
from django.utils.timezone import now
from appcuentas.models import *
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
    #registerform = RegisterForm()
    error = None
    vista = "register"
    if request.POST:
    #registerform = RegisterForm(request.POST)
    #if registerform.is_valid():
        nombre = request.POST.get('nombre', -1)
        apellidos = request.POST.get("apellidos", -1)
        email = request.POST.get("email", -1)
        profiles = Profile.objects.all()
        passw = request.POST.get("password", -1)
        repassw = request.POST.get("repassw", -1)
        if repassw == passw and email != -1 and apellidos != -1 and nombre != -1:
            u = User(username=nombre, first_name=nombre, last_name=apellidos, email=email)
            u.set_password(repassw)
            u.save()
            Client.objects.create(user=u, profile=profiles[0])
            request.session['registrado'] = True
            return redirect(to="/register")
        else:
            if repassw == passw:
                error = "los password no son iguales"
            else:
                error = "Falta insertar datos"
    mostrar = 0

    if request.session.get('registrado'):
        mostrar = 1
        del request.session['registrado']
    print error
    return render_to_response("desktop/inicio.html", {"error": error, 'mostrar': mostrar, 'vista': vista},
        context_instance=RequestContext(request))

login_required(login_url='/login/')

def view_change_password(request):
    error = ''
    if request.is_ajax():
        delete_pass = request.POST.get('password', '')
        passw = request.POST.get('password_new', '')
        repassw = request.POST.get('repassword_new', '')
        if delete_pass != '' and passw != '' and repassw != '':
            if passw == repassw:
                client = get_object_or_404(Client, user__id=request.user.id)
                user = client.user
                if user.check_password(delete_pass):
                    user.set_password(repassw)
                    user.save()
                    error = 'password cambiado correctamente'
                else:
                    error = 'password incorrecto'
            else:
                error = 'password diferente'
        else:
            error = "todos los campos son obligatorios"
    print error
    return HttpResponse(simplejson.dumps({'error': error}), mimetype='application/json')

login_required(login_url='/login/')

def view_change_datos(request):
    error = ''
    if request.is_ajax():
        nombre = request.POST.get('nombre_change_profile', '')
        apellidos = request.POST.get('apellido_change_profile', '')
        email = request.POST.get('email_change_profile', '')
        client = get_object_or_404(Client, user__id=request.user.id)
        user = client.user
        if nombre != '':
            user.first_name = nombre
        if apellidos != '':
            user.last_name = apellidos
        if email != '':
            user.email = email
        user.save()
    ext = "desktop/layout.html"
    return render_to_response("desktop/account.html", {'error': '', 'ext': ext, 'actual': 'account'},
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def view_home(request):
    if request.is_ajax():
        ext = "desktop/vacio.html"
    else:
        ext = "desktop/layout.html"
    proyectos1 = Client_has_Project.objects.filter(client__user=request.user)
    proyectos2 = Project.objects.filter(creador__user__id=request.user.id)
    proyectos = list(set(proyectos1).union(set(proyectos2)))[0:3]
    grupos = Group_has_Client.objects.filter(client__user=request.user)
    grupos = list(set(Group.objects.filter(creador=request.user.get_profile())).union(set(grupos)))[0:3]
    return render_to_response("desktop/home.html",
            {'ext': ext, 'actual': 'home', 'proyectos': proyectos, 'grupos': grupos},
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def view_projects(request):
    if request.is_ajax():
        ext = "desktop/vacio.html"
    else:
        ext = "desktop/layout.html"
    proyectos = Project.objects.filter(creador=request.user.get_profile()).order_by('-date_creation')
    chp = Client_has_Project.objects.filter(client=Client.objects.get(user=request.user))
    proyectos2 = set([proy.project for proy in chp])
    clients = Client.objects.exclude(user=request.user)
    return render_to_response("desktop/projects.html",
            {'ext': ext, 'actual': 'projects', 'proyectos': proyectos, 'proyectos2': proyectos2, 'clients': clients},
        context_instance=RequestContext(request))


@login_required(login_url='/login/')
def view_groups(request):
    if request.is_ajax():
        ext = "desktop/vacio.html"
    else:
        ext = "desktop/layout.html"
    grupos = Group.objects.filter(creador=request.user.get_profile()).order_by('-date_creation')
    clients = Client.objects.exclude(user=request.user)
    return render_to_response("desktop/groups.html",
            {'ext': ext, 'actual': 'groups', 'grupos': grupos, 'clients': clients},
        context_instance=RequestContext(request))


def view_find_client(request):
    clients = Client.objects.exclude(id=request.user.id)
    return render_to_response("desktop/contenido-buscar.html",
            {'clients': clients}, context_instance=RequestContext(request))


def view_create_project(request):
    try:
        error = {'nombre': []}
        if request.method == "POST":
            if request.POST.get('nombre'):
                nombre = request.POST.get('nombre')
                company = request.POST.get('company')
                if not Project.objects.filter(creador=request.user.get_profile(), name=nombre):
                    Project.objects.create(name=nombre, company=company, creador=request.user.get_profile())
                    return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
                else:
                    error['nombre'].append('Ya existe un proyecto con ese nombre')
            else:
                error['nombre'].append('Debe ingresar un nombre')
            return HttpResponse(simplejson.dumps({'estado': 0, 'error': error}), mimetype='application/json')
        else:
            return render_to_response("desktop/create-project.html", context_instance=RequestContext(request))
    except Exception, ex:
        print ex
        return HttpResponse(simplejson.dumps({'estado': 0, 'error': 'No se pudo crear el grupo'}),
            mimetype='application/json')


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

#la puta mare no te borres puto view ._.
def view_delete_project(request):
    try:
        if 'groupid' in request.GET:
            project = get_object_or_404(Project, id=request.GET.get('groupid'))
            project.delete()
            return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
    except Exception, ex:
        print ex
        return HttpResponse(simplejson.dumps({'estado': 0}), mimetype='application/json')


def view_leave_project(request):
    try:
        if 'groupid' in request.GET:
            project = get_object_or_404(Client_has_Project, client=request.user.get_profile(),
                project__id=request.GET.get('groupid'))
            project.delete()
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


def view_get_project(request):
    try:
        error = {'nombre': []}
        if request.method == "POST":
            if request.POST.get('nombre'):
                nombre = request.POST.get('nombre')
                company = request.POST.get('company')
                mi_project = Project.objects.get(creador=request.user.get_profile(), id=request.POST.get('groupid'))
                existeotro = Project.objects.filter(creador=request.user.get_profile(), name=nombre).exclude(
                    id=request.POST.get('groupid'))
                if existeotro:
                    error['nombre'].append('Ya existe un proyecto con ese nombre')
                elif mi_project:
                    mi_project.name = nombre
                    mi_project.company = company
                    mi_project.save()
                    users = request.POST.get('users')
                    projects = Client_has_Project.objects.filter(project__id=request.POST.get('groupid'))
                    for chg in projects:
                        chg.delete()
                    if users:
                        users = users.split(',')
                        for userid in users:
                            Client_has_Project.objects.create(
                                project=Project.objects.get(id=request.POST.get('groupid')),
                                client=Client.objects.get(user__id=userid))
                    return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
                else:
                    return HttpResponse(simplejson.dumps({'estado': 2, 'error': 'No se pudo editar'}),
                        mimetype='application/json')
            else:
                error['nombre'].append('Debe ingresar un nombre')
            return HttpResponse(simplejson.dumps({'estado': 0, 'error': error}), mimetype='application/json')
        else:
            project = Project.objects.get(id=request.GET.get('idgroup'))
            template = "desktop/get-project-otro.html" if project.creador != request.user.get_profile() else "desktop/get-project.html"
            projects = Client_has_Project.objects.filter(project__id=request.GET.get('idgroup'))
            clients = []
            for chp in projects:
                clients.append(chp.client)
            return render_to_response(template, {'clients': clients, 'project': project},
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


def view_groups_add_client(request):
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
    return HttpResponse(0, mimetype="application/json")


def view_projects_add_client(request):
    if request.GET.get('iduser') and request.GET.get('idgroup'):
        try:
            client = get_object_or_404(User, id=request.GET.get('iduser'))
            client = get_object_or_404(Client, user=client)
            proyecto = get_object_or_404(Project, id=request.GET.get('idgroup'))
            existe = Client_has_Project.objects.filter(client=client, project=proyecto)
            if not existe:
                Client_has_Project.objects.create(client=client, project=proyecto)
                return HttpResponse(1, mimetype="application/json")
            else:
                return HttpResponse(2, mimetype="application/json")
        except Exception, ex:
            print ex
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


def view_board(request):
    try:
        if request.GET.get('idboard'):
            board = get_object_or_404(Table, id=request.GET.get('idboard'))
            columnas = Column.objects.filter(table=board)
            paquetes = Work_Package.objects.filter(table=board)
            tareas = set()
            for paquete in paquetes:
                tareas = tareas.union(set(Task.objects.filter(work_package=paquete)))
            print(tareas)
            return render_to_response("desktop/board.html",
                    {'board': board, 'columnas': columnas, 'paquetes': paquetes, 'tareas': tareas}
                , context_instance=RequestContext(request))
        return Http404
    except Exception, ex:
        print ex


def view_get_boards(request):
    if request.GET.get('idgroup'):
        project = get_object_or_404(Project, id=request.GET.get('idgroup'))
        boards = Table.objects.filter(project=project)
    return render_to_response("desktop/boards.html", {'boards': boards, 'idproject': project.id},
        context_instance=RequestContext(request))


def view_create_board(request):
    error = {'nombre': []}
    if request.method == "POST":
        if request.POST.get('nombre'):
            nombre = request.POST.get('nombre')
            project = Project.objects.get(id=request.POST.get('idproject'))
            if not Table.objects.filter(project=project, name=nombre):
                Table.objects.create(name=nombre, columns=0, project=project)
                return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
            else:
                error['nombre'].append('Ya existe un tablero con ese nombre')
        else:
            error['nombre'].append('Debe ingresar un nombre')
        return HttpResponse(simplejson.dumps({'estado': 0, 'error': error}), mimetype='application/json')


def view_delete_board(request):
    if request.GET.get('idboard'):
        idboard = request.GET.get('idboard')
        table = Table.objects.get(id=idboard)
        table.delete()
        return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
    return HttpResponse(simplejson.dumps({'estado': 0}), mimetype='application/json')


@login_required(login_url="/login/")
def view_tables(request):
    if request.method == 'GET' and request.is_ajax():
        return render_to_response("desktop/tableros.html", context_instance=RequestContext(request))
    raise Http404


def view_move_task(request):
    if request.GET.get('idtask') and request.GET.get('idcolumn') and request.GET.get('pila'):
        task = Task.objects.get(id=request.GET.get('idtask'))
        print task.column, Column.objects.get(id=request.GET.get('idcolumn')), request.GET.get('pila')
        if task.column == Column.objects.get(id=request.GET.get('idcolumn')):
            return HttpResponse(simplejson.dumps({'estado': 0}), mimetype='application/json')
        elif task.column != None and task.column != Column.objects.get(
            id=request.GET.get('idcolumn')) and request.GET.get('pila') == "true":
            return HttpResponse(simplejson.dumps({'estado': 0}), mimetype='application/json')
        else:
            task.column = Column.objects.get(id=request.GET.get('idcolumn'))
            task.save()
            return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
    return HttpResponse(simplejson.dumps({'estado': 0}), mimetype='application/json')


@login_required(login_url="/login/")
def view_reuniones(request):
    if request.method == 'GET' and request.is_ajax():
        reuniones = Meeting.objects.filter(project__id=request.GET.get('project_id', ''))
        return render_to_response("desktop/reuniones.html",
                {'reuniones': reuniones, 'project': request.GET.get('project_id')},
            context_instance=RequestContext(request))
    raise Http404


@login_required(login_url="/login/")
def view_crear_reunion(request):
    try:
        print 'hola'
        if request.method == 'GET' and request.is_ajax():
            print 'hola'
            summary = request.GET.get('summary', '')
            description = request.GET.get('description', '')
            initial = now()#request.GET.get('initial',datetime.now())
            end = now()#request.GET.get('end',datetime.now())
            date_creation = now()
            project = Project.objects.filter(id=request.GET.get('project_id', ''))[0]
            reuniones = Meeting.objects.filter(project__id=request.GET.get('project_id', ''))
            print 'hola'
            Meeting.objects.create(summary=summary, description=description, initial=initial, end=end,
                date_creation=date_creation, project=project)
            print 'hola'
            return render_to_response("desktop/reuniones.html",
                    {'reuniones': reuniones, 'project': request.GET.get('project_id')},
                context_instance=RequestContext(request))
    except Exception, ex:
        print ex
    raise Http404


def view_create_column(request):
    if request.method == "POST" and request.POST.get('nombre') and request.POST.get('idtable'):
        nombre = request.POST.get("nombre")
        position = 0;
        tabla = Table.objects.get(id=request.POST.get('idtable'))
        Column.objects.create(name=nombre, position=position, table=tabla)
        return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')


def view_delete_column(request):
    if request.GET.get('columna'):
        columna = get_object_or_404(Column, id=request.GET.get('columna'))
        for tarea in columna.tareas.all():
            tarea.column = None;
            tarea.save()
        columna.delete()
        return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')


def view_create_paquete(request):
    if  request.method == "POST" and request.POST.get('nombre') and request.POST.get(
        'description') and request.POST.get(
        'prioridad') and request.POST.get('idtable'):
        nombre = request.POST.get("nombre")
        description = request.POST.get('description')
        prioridad = request.POST.get('prioridad')
        table = Table.objects.get(id=request.POST.get('idtable'))
        Work_Package.objects.create(name=nombre, description=description, prioridad=prioridad, table=table,
            project=table.project)
        return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')


def view_delete_paquete(request):
    if request.GET.get('paquete'):
        paquete = get_object_or_404(Work_Package, id=request.GET.get('paquete'))
        for tarea in paquete.tareas.all():
            tarea.column = None
            tarea.save()
        for tarea in paquete.tareas.all():
            tarea.delete()
        paquete.delete()
        return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')


def view_create_tarea(request):
    try:
        if  request.method == "POST" and request.POST.get('titulo') and request.POST.get(
            'description') and request.POST.get('paquete'):
            titulo = request.POST.get("titulo")
            description = request.POST.get('description')
            paquete = Work_Package.objects.get(id=request.POST.get('paquete'))
            column = Column.objects.filter(id=request.POST.get('column'))
            if not column: column = None
            Task.objects.create(title=titulo, subtitle=titulo, state="1", description=description, work_package=paquete,
                column=column)
            return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')
    except Exception, ex:
        print ex


def view_delete_tarea(request):
    if request.GET.get('tarea'):
        tarea = get_object_or_404(Task, id=request.GET.get('tarea'))
        tarea.delete();
        return HttpResponse(simplejson.dumps({'estado': 1}), mimetype='application/json')