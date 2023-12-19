from requests import post

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ZGU4MTlkZDliOGY0MGY3YTIzNzEyYzNjMDdiNWM3MiIsImlhdCI6MTcwMjQ5NjcxNCwiZXhwIjoyMDE3ODU2NzE0fQ.ij0wfcaBDsA1jv1Wiedn-IqkAqjcu6x-cksXuHuBpQg"
url = "http://192.168.1.80:8123/api/services/switch/turn_on"
headers = {"Authorization": "Bearer "+TOKEN}
data = {"entity_id": "switch.sonoff_1001da0402"}

response = post(url, headers=headers, json=data)
print(response.text)