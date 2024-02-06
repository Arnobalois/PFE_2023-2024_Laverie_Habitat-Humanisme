import enum
from django.db import models
from django.conf import settings

class Locataire(models.Model):
  class PermissionType(models.TextChoices):
    USER = "user"
    ADMIN = "admin"
  user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
  permission = models.CharField(max_length=255, choices=PermissionType.choices, default=PermissionType.USER,null=False)
  user_badge_id = models.CharField(max_length=255,null=True, blank=True)

class Machine(models.Model):

  class MachineType(models.TextChoices):
    SECHE_LINGE = "Sèche Linge"
    LAVE_LINGE = "Lave Linge"

  machine_id = models.IntegerField(null=False)
  available = models.BooleanField(null=False , default = False)
  sensor_id = models.CharField(max_length=255)
  typeMachine = models.CharField(max_length=255, choices=MachineType.choices, default=MachineType.LAVE_LINGE)
  running = models.BooleanField(null=False , default = False)
  SelectionDate = models.DateTimeField(null=True)

class Consomation(models.Model):
  comsumption_date = models.DateTimeField(null=False)
  user = models.ForeignKey(Locataire, on_delete=models.CASCADE)
  comsumption_duration = models.IntegerField(null = True)
  comsumption = models.IntegerField(null =False)