# Create your views here.

#from app_temp.models import Client,Group,Group_has_Client
from django.http import HttpResponse

def index(request):
    return  HttpResponse("vista de crear grupo")
    #return render_to_response('romell/index.html', )