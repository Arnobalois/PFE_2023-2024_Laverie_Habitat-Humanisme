from django.test import TestCase
from HomeAssistantAPI.tests import *
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Locataire, Machine, Consommation


class MachinesTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(machine_id=1, available=True, sensor_id='sensor123', typeMachine=Machine.MachineType.LAVE_LINGE, running=False)

    def test_machine_creation(self):
        self.assertEqual(self.machine.machine_id, 1)
        self.assertTrue(self.machine.available)
        self.assertEqual(self.machine.sensor_id, 'sensor123')
        self.assertEqual(self.machine.typeMachine, Machine.MachineType.LAVE_LINGE)
        self.assertFalse(self.machine.running)

class ConsommationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.machine = Machine.objects.create(machine_id=1, available=True, sensor_id='sensor123', typeMachine=Machine.MachineType.LAVE_LINGE, running=False)
        self.Consommation = Consommation.objects.create(comsumption_date=timezone.now(), user=self.user, machine = self.machine, comsumption_duration=30, comsumption=50)

    def test_Consommation_creation(self):
        self.assertEqual(self.Consommation.user, self.user)
        self.assertEqual(self.Consommation.comsumption_duration, 30)
        self.assertEqual(self.Consommation.comsumption, 50)