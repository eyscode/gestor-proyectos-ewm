# Create your views here.
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.utils import simplejson

def view_login_movil(request):
    to_json = -1
    if request.is_ajax() and request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                to_json = request.user.id
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
