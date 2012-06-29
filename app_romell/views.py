# Create your views here.

from django.http import HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from django.template import RequestContext
from django.core.files.uploadedfile import UploadedFile

def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def create_group(request):
    if request.method == 'POST':
        return redirect('home')
    else:
        return render_to_response('app_romell/group.html',context_instance=RequestContext(request))
    #raise 404

def upload_file(request):
    if request.method == 'POST':
        if request.FILES == None:
            return HttpResponseBadRequest('Must have files attached')
        file = request.FILES['file']
        file_name = UploadedFile(file).name
        return render_to_response('upload.html',{'description':'File saving done'})
    else:
        return HttpResponseRedirect('/login/')
    #raise 404