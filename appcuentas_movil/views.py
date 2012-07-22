# Create your views here.
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.utils import simplejson

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
