import  requests
from enum import Enum
from django.http import JsonResponse
from django.conf import settings
import json

class Services(Enum):
     TURN_ON = "turn_on"
     TURN_OFF = "turn_off"
class SensorType(Enum):
     SWITCH = "switch"
     SENSOR = "sensor"
class SensorRessource(Enum):
    SWITCH= "state"
    CURRENT = "current"
    CONSUMPTION= "energy_day"
    POWER ="power"

def getHomeAssistantAPIStatus():
      """
      Retrieves the status of the Home Assistant API.

      Returns:
            str: The response from the API, or an error message if the server is not responding.
      """
      url = settings.HA_SERVER + "/api/"
      headers = {"Authorization": "Bearer " + settings.HA_TOKEN,"content-type": "application/json",}
      try:
            response = requests.get(url, headers=headers, timeout=1)
      except(requests.ConnectionError, requests.Timeout):
            if (response.status_code == 401):
                  return {'Error':'Tokken incorrect ' }
            return {'Error': 'server not responding !'}
      
      response = json.dumps(response.text)

      return response

def getSensorState(sensor_id: str , Ressource : SensorRessource):
      """
      Retrieves the state of a sensor in Home Assistant.

      Args:
            sensor_id (str): The ID of the sensor.
            Ressource (SensorRessource): The resource type of the sensor.

      Returns:
            dict: The state of the sensor.

      Raises:
            dict: An error message if the resource doesn't exist or the server is not responding.
      """
      match Ressource:
            case SensorRessource.SWITCH:
                  url = settings.HA_SERVER + "/api/states/" + SensorType.SWITCH.value +"."+sensor_id
                  headers = {"Authorization": "Bearer "+settings.HA_TOKEN}
                          
            case SensorRessource.CURRENT:
                  url = settings.HA_SERVER + "/api/states/"+SensorType.SENSOR.value+ "."+sensor_id+"_"+Ressource.value
                  headers = {"Authorization": "Bearer "+settings.HA_TOKEN}

            case SensorRessource.CONSUMPTION:
                  url = settings.HA_SERVER + "/api/states/"+SensorType.SENSOR.value+ "."+sensor_id+"_"+Ressource.value
                  headers = {"Authorization": "Bearer "+settings.HA_TOKEN}
            case SensorRessource.POWER:
                  url = settings.HA_SERVER + "/api/states/"+SensorType.SENSOR.value+ "."+sensor_id+"_"+Ressource.value
                  headers = {"Authorization": "Bearer "+settings.HA_TOKEN}
            case _:
                  return {'Error':'Resource doesn\'t exist in Home Assistant' }
      try :
            response = requests.get(url, headers=headers, timeout=1)
      except(requests.ConnectionError, requests.Timeout):
            return {'Error': 'server not responding !'}
      if (response.status_code == 401):
            return {'Error':'Tokken incorrect ' }
      response = json.loads(response.text)
      if(response["state"] == "unavailable"):
            return {'Error':'Sensor not available'}
      
      return {'state': response["state"]}
            
            
def modifySensorState(id_sensor: str , Ressource : SensorRessource, state : Services ):
      """
      Modifies the state of a sensor in Home Assistant.

      Args:
            id_sensor (str): The ID of the sensor.
            Ressource (SensorRessource): The resource type of the sensor.
            state (Services): The desired state of the sensor.

      Returns:
            dict: The response from Home Assistant.

      Raises:
            Exception: If the server is not responding.

      """
      match Ressource:
            case SensorRessource.SWITCH:
                  url = settings.HA_SERVER + "/api/services/switch/"+state.value
                  headers = {"Authorization": "Bearer "+settings.HA_TOKEN}
                  data = {"entity_id": "switch." + id_sensor}
            case _:
                  return {'Error':'Resource doesn\'t exist in Home Assistant' }
      try :
            response = requests.post(url, headers=headers, json=data,timeout=1)
            return{'Status': response.status_code}
      except(requests.ConnectionError, requests.Timeout):
            return {'Error': 'server not responding !'}
      
            