from django.contrib import admin
from .models import Expansion,FFXIVJob

# Register your models here.

admin.site.register(FFXIVJob)
admin.site.register(Expansion)