from django.shortcuts import render,get_object_or_404
from practise.models import *
from practise.forms import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def Home(request):
    return render(request,"index.html")

@login_required
def index(request):
    if request.method == "POST":
        form = Info_form(request.POST)
        ob = Info.objects.all()
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            print(email)
            return render(request,"index.html")
        else:
            print(form.errors)
    else:
        form = Info_form()
    return render(request,"index0.html",{'form':form})

@login_required
def feedback_web(request):
    link = "http://127.0.0.1:8000/crontab/feedback/"
    name = request.user.username
    email = request.user.email
    if request.method == "POST":
        services = request.POST['services']
        Guide = request.POST['guide']
        Query = request.POST.get('query', False)
        ob = feed.objects.create(name = name,email = email,services = services,Guide = Guide,Query = Query)
        ob.save()
        return render(request,"timer.html",{'link':link})

    return render(request,"feedback.html",{'name':name,'email':email})
