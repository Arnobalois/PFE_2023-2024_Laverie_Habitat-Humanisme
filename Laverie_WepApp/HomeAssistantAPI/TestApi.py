from HomeAssistant import *

sensor_id = "sonoff_1001da0402"
url = "http://192.168.1.80:8123" + "/api/states/"+ "switch."+ sensor_id
headers = {"Authorization": "Bearer "+ "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ZGU4MTlkZDliOGY0MGY3YTIzNzEyYzNjMDdiNWM3MiIsImlhdCI6MTcwMjQ5NjcxNCwiZXhwIjoyMDE3ODU2NzE0fQ.ij0wfcaBDsA1jv1Wiedn-IqkAqjcu6x-cksXuHuBpQg"}

response = get(url, headers=headers)

response = json.loads(response.text)
print(response['state'])