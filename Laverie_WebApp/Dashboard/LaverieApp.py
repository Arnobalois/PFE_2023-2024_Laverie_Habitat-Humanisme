from .models import Machine , Consommation
from HomeAssistantAPI import HomeAssistant
from django.contrib.auth.models import  User
import json
import threading
import time
def updateDatabase():
    """
    Updates the availability status of machines in the database based on their sensor state.
    """
    if(Machine.objects.all().exists()):
        nombreMachine = Machine.objects.count()
        for i in range(nombreMachine):
            currentMachine = Machine.objects.all()[i]
            response = HomeAssistant.getSensorState(currentMachine.sensor_id,HomeAssistant.SensorRessource.SWITCH)
            print(response)
            if 'Error' in response.keys(): 
                currentMachine.available = False
            else:
                currentMachine.available = True if response["state"] == 'off' else False
            currentMachine.save()

def startProcess(machine_id,User):
    """
    Starts the laundry process for the specified machine.

    Args:
        machine_id (int): The ID of the machine.

    Returns:
        bool: True if the process is successfully started, False otherwise.
    """
    if HomeAssistant.getHomeAssistantAPIStatus() == {'Error': 'server not responding !'}:
        return False
    currentMachine = Machine.objects.get(id = machine_id)
    if currentMachine is None:
        return False
    if HomeAssistant.getSensorState(currentMachine.sensor_id,HomeAssistant.SensorRessource.SWITCH) == {'Error': 'server not responding !'}:
        return False
    if currentMachine.available == True and currentMachine.running == False:
        my_thread = threading.Thread(target=cycle_en_cours_Thread,args=(machine_id,User,))
        my_thread.start()
        return True
    else:
        return False


def cycle_en_cours_Thread(machine_id, User):
    """
    Function to run a laundry cycle on a specific machine.

    Args:
        machine_id (int): The ID of the machine.
        id_user (int): The ID of the user.

    Returns:
        bool: True if the cycle was completed successfully, False otherwise.
    """

    currentMachine = Machine.objects.get(id=machine_id)
    currentMachine.available = False
    currentMachine.RemainingTime = 20
    currentMachine.save()

    HomeAssistant.modifySensorState(currentMachine.sensor_id, HomeAssistant.SensorRessource.SWITCH, HomeAssistant.Services.TURN_ON)
    while currentMachine.RemainingTime > 0:
        print(float(HomeAssistant.getSensorState(currentMachine.sensor_id, HomeAssistant.SensorRessource.POWER)["state"]))
        if float(HomeAssistant.getSensorState(currentMachine.sensor_id, HomeAssistant.SensorRessource.POWER)["state"]) > 10.0:
            currentMachine.running = True
            currentMachine.RemainingTime = 60
            currentMachine.save()
            break
        time.sleep(10)
        currentMachine.RemainingTime -= 0.17
        v.save()

    if currentMachine.running:
        StartingDate = time.time()
        currentcosumption = 0 
        comsumptionDataBase = Consommation.objects.create( user=User, machine=currentMachine, comsumption_duration=0, comsumption=0)
        while True:
            currentPower = float( HomeAssistant.getSensorState(currentMachine.sensor_id, HomeAssistant.SensorRessource.POWER)["state"])
            if  currentPower < 5.0:
                comsumptionDataBase.comsumption_duration = time.time() - StartingDate
                comsumptionDataBase.comsumption = currentcosumption
                comsumptionDataBase.save()
                break

            currentcosumption+= (currentPower/1000)*0.0278 #Conversion de Watt Seconde en kWh
            currentMachine.RemainingTime -= 0.17
            currentMachine.save()
            time.sleep(10)


    HomeAssistant.modifySensorState(currentMachine.sensor_id, HomeAssistant.SensorRessource.SWITCH, HomeAssistant.Services.TURN_OFF)
    currentMachine.running = False
    currentMachine.available = True
    currentMachine.RemainingTime = 0
    currentMachine.save()

    return True
