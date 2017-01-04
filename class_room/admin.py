from django.contrib import admin
from .models import BaseClass,BaseJob,Base,Job,Role,Expansion,Level,Stat

# Register your models here.

admin.site.register(BaseClass)
admin.site.register(BaseJob)
admin.site.register(Role)
admin.site.register(Expansion)
admin.site.register(Level)
admin.site.register(Stat)
admin.site.register(Base)
admin.site.register(Job)
