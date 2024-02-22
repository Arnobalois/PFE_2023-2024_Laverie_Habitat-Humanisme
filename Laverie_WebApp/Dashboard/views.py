import json
import csv
from django.contrib.auth.models import  User
from django.contrib.auth import  authenticate , login ,logout
from django.shortcuts import render
from django.template import loader
from .models import Consommation, Machine
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from . import forms , LaverieApp
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods , require_safe



# Create your views here.

@login_required(login_url='/Login')
def Accueil(request):
    template = loader.get_template('Accueil.html')
    if request.user.is_superuser:
        context = {'admin' : True}
    else:
        context = {'admin' : False}
    if(Machine.objects.all().exists()):
       # LaverieApp.updateDatabase()
        myMachines = Machine.objects.all().values()
        context['myMachines'] = myMachines
    return HttpResponse(template.render(context, request))

@require_http_methods(["POST","GET"])
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
                print("je suis ici")
                return redirect("Accueil")
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'Login.html', context={'form': form, 'message': message})
  else : 
      return redirect("Accueil")

@login_required(login_url='')
def logout_user(request):
    logout(request)
    return redirect("Login")

@login_required(login_url='/Login')
@require_safe
def update(request):
        if request.method == "GET":
            LaverieApp.updateDatabase()
            response =  list(Machine.objects.values_list('id','available'))
            response = json.dumps(response)  
            return HttpResponse(response)
        elif request.method =="POST":
            return {"status": 'failed'} 

@login_required(login_url='')  
@require_http_methods(["POST"])      
def start(request):
    if request.method == "GET":
            return {"status": 'Failed'} 
    elif request.method == "POST":
            start = LaverieApp.startProcess(request.POST.get("MachineID",""))
    return JsonResponse({"status": 'success',"started" : start})

@login_required(login_url='/Login')
@require_safe
@staff_member_required
def Admin(request):
    template = loader.get_template('Administration.html')
    users = User.objects.all()
    consumptions = []
    years = []
    for user in users :
            consumption ={'Prenom' : user.first_name}
            consumption["Nom"]= user.last_name
            consumption["PeriodeYears"]=[]
            consumption["PeriodeMonths"]=[]
            if Consommation.objects.filter(user_id =user.pk ).exists():
                consumptionsRequested = Consommation.objects.filter(user=user.pk).all()
                for cons in consumptionsRequested:
                    if cons.comsumption_date.year not in consumption["PeriodeYears"]:
                        consumption["PeriodeYears"].append(cons.comsumption_date.year)
                        if cons.comsumption_date.year not in years : 
                             years.append(cons.comsumption_date.year)
                    if cons.comsumption_date.month not in consumption["PeriodeMonths"]: 
                        consumption["PeriodeMonths"].append(cons.comsumption_date.month)
            consumptions.append(consumption)    
    context = {'consumptions' : consumptions}
    context["Periodes"] = years
    return HttpResponse(template.render(context, request))

@login_required(login_url='/Login')
@staff_member_required
@require_http_methods(["POST"])
def Convert(request):
    print(request.POST)
    if len(request.POST) == 0 : 
     print("je suis vide")
     
    
    for data in request.POST:
        newdata=json.loads(data)
        for tinydata in newdata:
            print(tinydata["Nom"])
        

    #response = HttpResponse(content_type="text/csv")
    #response["Content-Disposition"] = 'attachment; filename="somefilename.csv"'
    
     
    #writer = csv.writer(response)
    #writer.writerow(["Nom","Prenom","Annees"])
    #return response
    return JsonResponse({"status": 'Failed'})