# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from app_temp.models import Client, User
from app_temp.forms import RegisterForm

def view_login(request):
	error = None
	if request.POST:
		usuario = request.POST.get("username","")
		password = request.POST,get("password","")
		if usuario and password:
			user = authenticate(usuario, password)
			if user is not None:
				login(request, user)
				return redirect(to="/board")
			else:
				error = "Su password o usuario es incorrecto"
	return render_to_response("login.html",{"error":error},context_instance=RequestContext(request))
 
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
			u = User.objects.create(nombre,apellidos,email)
			Client.objects.create(user=u, profile=perfil)
			return redirect(to="/board")
	return render_to_response("register.html", {"rf":registerform}, context_instance=RequestContext(request))

 @login_required(redirect_to="/login")
 def view_board(request):
 	#TODO: logic of board
 	return render_to_response("board.html",context_instance=RequestContext(request))