from .models import Machine
from HomeAssistantAPI import HomeAssistant
import json
import threading
import time

def updateDatabase():

    if(Machine.objects.all().exists()):
        nombreMachine = Machine.objects.count()
        for i in range(nombreMachine):
            currentMachine = Machine.objects.all()[i]
            response = HomeAssistant.getSensorState(currentMachine.machine_id,HomeAssistant.SensorRessource.SWITCH)
            response = json.loads(response.text)
            currentMachine.available = True if response["state"] == 'on' else False
            currentMachine.save()

def startProcess(sensor_id):
    currentMachine = Machine.objects.get(id = sensor_id)
    if currentMachine.available == False and currentMachine.running == False:
        #lancer un thread 
        my_thread = threading.Thread(target=cycle_en_cours_Thread,args=(sensor_id,))
        my_thread.start()
        currentMachine.available = True
        currentMachine.save()
        print("Thread lancé")
        return True
    else:
        print("Cette machine est déja en cours d'utilisation")
        return False


def cycle_en_cours_Thread(machine_id):
    currentMachine = Machine.objects.get(id = machine_id)
    print("Thread started.")
    HomeAssistant.modifySensorState(currentMachine.sensor_id,HomeAssistant.SensorRessource.SWITCH,HomeAssistant.Services.TURN_ON)
    time.sleep(50)
    print("Thread terminating.")
    HomeAssistant.modifySensorState(currentMachine.sensor_id,HomeAssistant.SensorRessource.SWITCH,HomeAssistant.Services.TURN_OFF)
    print(currentMachine)
    currentMachine.available = False
    currentMachine.save()
    print("Fin de modification disponibilité")

#Thread : lancer un chrono de 10 min durant lequel on fait des requête vers HA pour verifier si il y a une monté en tension
#des qu'on vois l'apparition du patern on envoi un signal pour indiquer que la machine est bien prise 
#par la suite on vien interoger HA toute les mins pour verifier qu'on est pas a l'arrêt 
    #si la machine s'arrete on modifie la valeur en bdd et on kill le thread 