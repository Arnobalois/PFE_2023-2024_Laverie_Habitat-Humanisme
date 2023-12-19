from requests import get
import json
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2ZGU4MTlkZDliOGY0MGY3YTIzNzEyYzNjMDdiNWM3MiIsImlhdCI6MTcwMjQ5NjcxNCwiZXhwIjoyMDE3ODU2NzE0fQ.ij0wfcaBDsA1jv1Wiedn-IqkAqjcu6x-cksXuHuBpQg"
url = "http://192.168.1.80:8123/api/states/switch.sonoff_1001da0402"
headers = {
    "Authorization": "Bearer " + token,
    "content-type": "application/json",
}
response = get(url, headers=headers)
response = json.loads(response.text)
print(response["state"])                                                                           
