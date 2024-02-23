
import datetime
import enum
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Machine(models.Model):

  class MachineType(models.TextChoices):
    SECHE_LINGE = "Sèche Linge"
    LAVE_LINGE = "Lave Linge"

  machine_id = models.IntegerField(null=False)
  available = models.BooleanField(null=False , default = False)
  sensor_id = models.CharField(max_length=255)
  typeMachine = models.CharField(max_length=255, choices=MachineType.choices, default=MachineType.LAVE_LINGE)
  running = models.BooleanField(null=False , default = False)
  RemainingTime = models.IntegerField(null=True , default=0)

class Consommation(models.Model):
  comsumption_date = models.DateTimeField(null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
  machine = models.ForeignKey(Machine, on_delete=models.CASCADE,null=True)
  comsumption_duration = models.IntegerField(null = True)
  comsumption = models.FloatField(null =False)