import json
from django.test import TestCase
from django.conf import settings
from requests import get, post
from Dashboard.models import Machines

class HomeAssistantAPITest(TestCase):
    def init(self):
        MachineTest = Machines()


    def test_HomeAssistant_API_Connection(self):
        url = settings.HA_SERVER + "/api/"
        headers = {"Authorization": "Bearer " + settings.HA_TOKEN,"content-type": "application/json",}
        try :
            response = get(url, headers=headers)
        except :
            self.assertTrue(False)
        print(response.json())
        self.assertEqual(response.json(),{"message": "API running."})
        self.assertNotEqual(404,response.status_code)
        self.assertNotEqual(403,response.status_code)
        self.assertNotEqual(402,response.status_code)

    def test_HomeAssitante_API_GET_Sensor_STATE(self):
        self.assertTrue