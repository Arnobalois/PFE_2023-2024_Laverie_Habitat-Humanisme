from django.test import TestCase
from HomeAssistantAPI.tests import *
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Locataire, Machine, Consomation

class LocatairesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.locataire = Locataire.objects.create(user=self.user, user_badge_id='123')

    def test_locataire_creation(self):
        self.assertEqual(self.locataire.user, self.user)
        self.assertEqual(self.locataire.user_badge_id, '123')

class MachinesTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(machine_id=1, available=True, sensor_id='sensor123', typeMachine=Machine.MachineType.LAVE_LINGE, running=False)

    def test_machine_creation(self):
        self.assertEqual(self.machine.machine_id, 1)
        self.assertTrue(self.machine.available)
        self.assertEqual(self.machine.sensor_id, 'sensor123')
        self.assertEqual(self.machine.typeMachine, Machine.MachineType.LAVE_LINGE)
        self.assertFalse(self.machine.running)

class ConsomationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.locataire = Locataire.objects.create(user=self.user, user_badge_id='123')
        self.machine = Machine.objects.create(machine_id=1, available=True, sensor_id='sensor123', typeMachine=Machine.MachineType.LAVE_LINGE, running=False)
        self.consomation = Consomation.objects.create(comsumption_date=timezone.now(), user=self.locataire, comsumption_duration=30, comsumption=50)

    def test_consomation_creation(self):
        self.assertEqual(self.consomation.user, self.locataire)
        self.assertEqual(self.consomation.comsumption_duration, 30)
        self.assertEqual(self.consomation.comsumption, 50)