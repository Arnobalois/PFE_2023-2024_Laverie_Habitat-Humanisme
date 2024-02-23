import json
from django.test import TestCase
from django.conf import settings
from requests import get, post
from .HomeAssistant import *
from django.http import JsonResponse

class HomeAssistantServerConnectionTest(TestCase):

    def test_HomeAssistant_API_Connection(self):
        response = getHomeAssistantAPIStatus()
        self.assertEqual(response,'"{\\"message\\":\\"API running.\\"}"')

class HomeAssistantAPITest(TestCase):
    
    def setUp(self):
        self.sensor_id = "sonoff_1001da0402"

    def test_HomeAssitante_API_GET_Sensor_STATE(self):

        response = getSensorState(self.sensor_id,SensorRessource.SWITCH)
        print(response)
        self.assertTrue(((response == "on") or (response == "off")))



