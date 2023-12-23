from django.contrib import admin
from .models import Machines, Locataires , Consomation

# Register your models here.
admin.site.register(Machines)
admin.site.register(Locataires)
admin.site.register(Consomation)