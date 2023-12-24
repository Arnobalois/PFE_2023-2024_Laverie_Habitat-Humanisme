from django.contrib import admin
from .models import Machine, Locataire , Consomation

# Register your models here.
admin.site.register(Machine)
admin.site.register(Locataire)
admin.site.register(Consomation)