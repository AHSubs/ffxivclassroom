from django.db import models
from django.utils import timezone

# Create your models here.

class Expansion(models.Model):
    AVAIL = (
        ('ARR', 'A Realm Reborn'),
        ('HW', 'Heavensward'),
        ('SB', 'Storm Blood')
    )
    expansion_name = models.CharField(max_length=20,choices=AVAIL)

    def __str__(self):
        return self.expansion_name

class FFXIVJob (models.Model):

    name = models.CharField(max_length=80,null=False)
    role = models.ForeignKey('ffxivclass.RoleSelect')
    lore = models.TextField(null=True)
    icon = models.CharField(max_length=255,null=True)
    available  = models.ForeignKey('Expansion')
    creation_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name,self.lore,self.icon
