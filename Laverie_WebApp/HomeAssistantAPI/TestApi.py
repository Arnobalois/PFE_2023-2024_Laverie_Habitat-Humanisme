from HomeAssistant import *

sensor_id = "sonoff_1001da0402"
url = "http://192.168.1.80:8123" + "/api/states/"+ "switch."+ sensor_id
headers = {"Authorization": "Bearer "+ "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxM2IxZTkzMWY5NmM0NGRiOTgyZWI4NDcyNjliMDdkZSIsImlhdCI6MTcwODg4NzI2NiwiZXhwIjoyMDI0MjQ3MjY2fQ.dwMJCZvQ3PCuHwE7fpcagpNCNBMCzf9yFn5c_5pUbpA"}

response = requests.get(url, headers=headers)

print(response.text)

url = "http://192.168.1.80:8123" + "/api/services/switch/"+Services.TURN_ON.value
data = {"entity_id": "switch." + sensor_id}
response = requests.post(url, headers=headers, json=data)
print(response.status_code)

#url = "http://192.168.1.80:8123" + "/api/states/"+ "switch."+ sensor_id
#response = get(url, headers=headers)

url = "http://192.168.1.80:8123"+ "/api/states/"+SensorType.SENSOR.value+ "."+sensor_id+"_"+ SensorRessource.POWER.value
response = requests.get(url, headers=headers)

print(response.text)