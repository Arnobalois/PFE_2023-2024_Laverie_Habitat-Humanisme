from requests import get, post
from Dashboard.models import Machines
from enum import Enum
from django.conf import settings
import json

class Services(Enum):
     TURN_ON = "turn_on"
     TURN_OFF = "turn_off"
class SensorType(Enum):
     SWITCH = "switch"
     SENSOR = "sensor"
class SensorRessource(Enum):
    SWITCH= "switch"
    CURRENT = "current"
    CONSUMTION= "energy_day"
   

def getSensorState(sensor_id: str , Ressource : SensorRessource):
        match Ressource:
          case SensorRessource.SWITCH:
                url = settings.HA_SERVER + "/api/states/"
                headers = {"Authorization": "Bearer "+settings.HA_TOKEN}
                data = {"entity_id": SensorType.SWITCH.value+"."+sensor_id}
                response = post(url, headers=headers, json=data)
                print(response.text)
                return response.text
          case SensorRessource.CURRENT:
                url = settings.HA_SERVER + "/api/states/"
                headers = {"Authorization": "Bearer "+settings.HA_TOKEN}
                data = {"entity_id": SensorType.SENSOR.value+ "."+sensor_id+"_"+Ressource.value}
                response = post(url, headers=headers, json=data)
                print(response.text)
                return response.text
    
          case _:
            print("Erreur")
            
            
def modifySensorState(id_sensor: str , Ressource : SensorRessource, state : Services ):
     match Ressource:
          case SensorRessource.SWITCH:
                print(id_sensor)
                url = settings.HA_SERVER + "/api/services/switch/"+state.value
                headers = {"Authorization": "Bearer "+settings.HA_TOKEN}
                data = {"entity_id": Ressource.value +"."+id_sensor}
                response = post(url, headers=headers, json=data)
                print(response.text)
                return response.text
          
          case _:
            print("Erreur")
            