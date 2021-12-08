from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import connection
from .forms import UploadFileForm

from .populate import populate

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            populate(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        
    else:
        print('notvalid')
        form = UploadFileForm()
    return render(request, 'databaseupdate/upload.html', {'form': form})