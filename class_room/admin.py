from django.contrib import admin
from .models import BaseClass,BaseJob,Base,Job,Role,Expansion,Level,Stat

# Register your models here.


class BaseAdmin(admin.ModelAdmin):

    displaybase = ('name','role','avail','lore','transformin','trasforminjobat','icon','creat_date','pub_date','stat')
    filterbase = ('role','avail','stat')

    list_display = displaybase
    list_filter = filterbase

class JobAdmin(admin.ModelAdmin):
    displayjob = ('name','role','avail','lore','transfrom1','transfrom2','icon','creat_date','pub_date','stat')
    filterjob = ('role','avail','stat')
    list_display = displayjob
    list_filter = filterjob

admin.site.register(BaseClass)
admin.site.register(BaseJob)
admin.site.register(Role)
admin.site.register(Expansion)
admin.site.register(Level)
admin.site.register(Stat)
admin.site.register(Base,BaseAdmin)
admin.site.register(Job,JobAdmin)
