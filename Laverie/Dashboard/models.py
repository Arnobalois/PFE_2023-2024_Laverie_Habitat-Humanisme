from django.db import models

# Create your models here.
class Locataires(models.Model):
  Nom = models.CharField(max_length=255,null=False)
  Prenom = models.CharField(max_length=255,null=False)
  ID_Badge = models.CharField(max_length=255,null=True)
  
class Machines(models.Model):
  Numero_Machine = models.IntegerField(null=False)
  Active = models.BooleanField(null=False)
  ID_Capteur = models.CharField(max_length=255)
