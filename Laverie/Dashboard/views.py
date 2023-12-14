from django.contrib.auth import  authenticate , login ,logout
from django.shortcuts import render
from django.template import loader
from .models import Machines
from django.shortcuts import redirect
from django.http import HttpResponse
from . import forms


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
      template = loader.get_template('DashboardTest.html')
      if(Machines.objects.all().exists()):
          myMachines = Machines.objects.all().values()
          print(myMachines)
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