import enum
from django.db import models
from django.conf import settings

class Locataires(models.Model):
  user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )
  user_badge_id = models.CharField(max_length=255,null=True, blank=True)
  
# Table qui permet de decrire une machine qui est présent dans la laverie
# Chaque machine est associé a un capteur
class Machines(models.Model):
  #MachineType est un enum qui permet de spécifié le type de la machine présente dans la laverie
  class MachineType(models.TextChoices):
    SECHE_LINGE = "Sèche Linge"
    LAVE_LINGE = "Lave Linge"

  machine_id = models.IntegerField(null=False)
  available = models.BooleanField(null=False , default = False)
  sensor_id = models.CharField(max_length=255)
  typeMachine = models.CharField(max_length=255, choices=MachineType.choices, default=MachineType.LAVE_LINGE)
  running = models.BooleanField(null=False , default = False)

#Table qui permet de sauvegarder la consomation des utilisateurs
class Consomation(models.Model):
  comsumption_date = models.DateTimeField(null=False)
  user = models.ForeignKey(Locataires, on_delete=models.CASCADE)
  comsumption_duration = models.IntegerField(null = True)
  comsumption = models.IntegerField(null =False)