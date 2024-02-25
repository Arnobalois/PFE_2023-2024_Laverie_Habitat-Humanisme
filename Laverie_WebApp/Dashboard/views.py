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
from HomeAssistantAPI import HomeAssistant


# Create your views here.

@login_required(login_url='/Login')
def Accueil(request):
    """
    Renders the Accueil.html template and returns the HttpResponse object.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HttpResponse: The rendered template with the context.

    """
    template = loader.get_template('Accueil.html')
    if request.user.is_superuser:
        context = {'admin' : True}
    else:
        context = {'admin' : False}
    if(Machine.objects.all().exists()):
        LaverieApp.updateDatabase()
        myMachines = Machine.objects.all().values()
        context['myMachines'] = myMachines
    return HttpResponse(template.render(context, request))

@require_http_methods(["POST","GET"])
def login_page(request):
    """
    Renders the login page and handles the login functionality.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered login page.
    """
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
                    login(request, user)
                    print("je suis ici")
                    return redirect("Accueil")
                else:
                    message = 'Identifiants invalides.'
        return render(
            request, 'Login.html', context={'form': form, 'message': message})
    else:
        return redirect("Accueil")

@login_required(login_url='')
def logout_user(request):
    """
    Logs out the user and redirects to the login page.

    Args:
        request: The HTTP request object.

    Returns:
        A redirect response to the login page.
    """
    logout(request)
    return redirect("Login")

@login_required(login_url='/Login')
@require_safe
def update(request):
    """
    This function handles the update request.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is GET, it returns a JSON response containing the list of machines and their availability.
    - If the request method is POST, it returns a dictionary with a 'status' key set to 'failed'.
    """
    if request.method == "GET":
        LaverieApp.updateDatabase()
        response =  list(Machine.objects.values_list('id','available','RemainingTime'))
        response = json.dumps(response)  
        return HttpResponse(response)
    elif request.method =="POST":
        return {"status": 'failed'}

@login_required(login_url='')  
@require_http_methods(["POST"])      
def start(request):
    """
    This function handles the start process for the laundry machine.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the status of the start process.
    """
    if request.method == "GET":
        return {"status": 'Failed'} 
    elif request.method == "POST":
        
        start = LaverieApp.startProcess(request.POST.get("MachineID",""),request.user.pk)
    return JsonResponse({"status": 'success',"started" : start})

@login_required(login_url='/Login')
@require_safe
@staff_member_required
def Admin(request):
    """
    Renders the Administration page with user consumption data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    template = loader.get_template('Administration.html')
    users = User.objects.all()
    consumptions = []
    years = []
    for user in users:
        consumption = {'FirstName': user.first_name}
        consumption["LastName"] = user.last_name
        consumption["id"] = user.pk
        consumption["PeriodeYears"] = []
        consumption["PeriodeMonths"] = []
        if Consommation.objects.filter(user_id=user.pk).exists():
            consumptionsRequested = Consommation.objects.filter(user=user.pk).all()
            for cons in consumptionsRequested:
                if cons.comsumption_date.year not in consumption["PeriodeYears"]:
                    consumption["PeriodeYears"].append(cons.comsumption_date.year)
                    if cons.comsumption_date.year not in years:
                        years.append(cons.comsumption_date.year)
                if cons.comsumption_date.month not in consumption["PeriodeMonths"]:
                    consumption["PeriodeMonths"].append(cons.comsumption_date.month)
        consumptions.append(consumption)
    context = {'consumptions': consumptions}
    context["Periodes"] = years
    return HttpResponse(template.render(context, request))

@login_required(login_url='/Login')
@staff_member_required
@require_http_methods(["POST"])
def Convert(request):
    print(request.POST)
    if len(request.POST) == 0 : 
        return JsonResponse({"status": 'Failed'})
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="somefilename.csv"'
    for data in request.POST:
        newdata=json.loads(data)
        writer = csv.writer(response)
        writer.writerow(["Nom","Prenom","Date_Consomation","Consommation","Duree_Consomation","id_Machine","Type_Machine"])
        for tinydata in newdata:
            if tinydata["Id"] == "all":
                users = User.objects.all()
                if users.exists():
                    for user in users:
                        userConsumptions = Consommation.objects.filter(user_id=user.pk).all()
                        for consumption in userConsumptions:
                            if tinydata["Years"] == "all" or tinydata["Years"] == str(consumption.comsumption_date.year): 
                                writer.writerow([user.last_name,user.first_name,consumption.comsumption_date,consumption.comsumption,consumption.comsumption_duration,consumption.machine.machine_id,consumption.machine.typeMachine])
                else:
                    return JsonResponse({"status": 'No data'})
            else:
                userConsumptions = Consommation.objects.filter(user_id=tinydata["Id"]).all()
                if userConsumptions.exists():
                    for consumption in userConsumptions:
                        if tinydata["Years"] == "all" and str(consumption.comsumption_date.month) == tinydata["Months"] or tinydata["Months"] == "all" and str(consumption.comsumption_date.year) == tinydata["Years"] or str(consumption.comsumption_date.year) == tinydata["Years"] and str(consumption.comsumption_date.month) == tinydata["Months"] or tinydata["Years"] == "all" and tinydata["Months"] == "all":
                            writer.writerow([tinydata["last_name"],tinydata["first_name"],consumption.comsumption_date,consumption.comsumption,consumption.comsumption_duration,consumption.machine.machine_id,consumption.machine.typeMachine])
        return response

@login_required(login_url='/Login')
@require_safe
@staff_member_required
def ServerStatus(request):
    """
    Retrieves the status of the Home Assistant API.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: The response from the API, or an error message if the server is not responding.
    """
    response = HomeAssistant.getHomeAssistantAPIStatus()
    return JsonResponse(response)