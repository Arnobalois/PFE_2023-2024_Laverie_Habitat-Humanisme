import json
from django.contrib.auth import  authenticate , login ,logout
from django.shortcuts import render
from django.template import loader
from .models import Machines
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, QueryDict
from . import forms
from HomeAssistantAPI import HomeAssistant
from Laverie import Laverie
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
      template = loader.get_template('Dashboard.html')
      if(Machines.objects.all().exists()):
          #HomeAssistant.updateDatabase()
          myMachines = Machines.objects.all().values()
          context = {'myMachines': myMachines,}
     
          return HttpResponse( template.render(context, request))
      return HttpResponse(template.render(None, request))
    else : 
      return redirect("Login")
    
def login_page(request):
  if not request.user.is_authenticated:
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                return redirect("Dashboard")
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'Login.html', context={'form': form, 'message': message})
  else : 
      return redirect("Dashboard")
  
def logout_user(request):
     logout(request)
     return redirect("Login")


def update(request):
    if request.user.is_authenticated:
        if request.method == "GET":
           # HomeAssistant.updateDatabase()
            response =  list(Machines.objects.values_list('id','available'))
            response = json.dumps(response)  
            print(response)
            return HttpResponse(response)
        elif request.method == "POST":
            print("Post request")
    else : 
      return redirect("Dashboard")
        
def start(request):
    if request.method == "GET":
            print("Get request")
            return JsonResponse({"status": 'Failed'}) 
    elif request.method == "POST":
            print("Post request")
            print(request.POST.get("MachineID",""))
            start = Laverie.startProcess(request.POST.get("MachineID",""))
    return JsonResponse({"Status": 'Success',"Started" : start}) 
