from HomeAssistant import *

sensor_id = "sonoff_1001da0402"
url = "http://192.168.1.80:8123" + "/api/states/"+ "switch."+ sensor_id
headers = {"Authorization": "Bearer "+ "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI5YmIwYzlhNWU0ZTQ0MTY1OGMzNjMxZGVjZmRjNjE2MCIsImlhdCI6MTcwMjQ5NzA3NCwiZXhwIjoyMDE3ODU3MDc0fQ.FKq6IY3mgHKcqkh2Vxtjq_5fPRS-edzKsfN0qubkVLg"}

response = get(url, headers=headers)

response = json.loads(response.text)
print(response['state'])

url = "http://192.168.1.80:8123" + "/api/services/switch/"+Services.TURN_ON.value
data = {"entity_id": "switch." + sensor_id}
response = post(url, headers=headers, json=data)

url = "http://192.168.1.80:8123" + "/api/states/"+ "switch."+ sensor_id
response = get(url, headers=headers)

response = json.loads(response.text)
print(response['state'])