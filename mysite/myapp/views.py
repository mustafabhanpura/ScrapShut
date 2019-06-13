from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template import RequestContext
from .models import Detail
from .forms import Page
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

def input_form(request):
    if request.method == 'POST':
         name = request.POST.get('name')
         email = request.POST.get('email')
         phone_number = request.POST.get('contact')
         image = request.FILES.get('image')
         video = request.FILES.get('video')
         stream = request.POST.get('stream')
         print(image)
         form = Detail.objects.create(name=name,email=email,phone_number = phone_number,image=image,video=video,stream=stream)
         form.save()

         return redirect('content/')
    return render(request,'myapp/homepage.html')
def display(request):

    everything = Detail.objects.all()


    return render(request,'myapp/test.html',{'everything':everything})

def delete(request,pk):
    Detail.objects.filter(id=pk).delete()

    return redirect('/myapp/content')

