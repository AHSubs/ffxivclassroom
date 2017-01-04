from django.db import models
from django.utils import timezone


# Create your models here.

class RoleSelect(models.Model):
    ROLE_CHOICES = (
        ('TANK', 'Tank'),
        ('DPS', 'Dps'),
        ('HEAL', 'Healer'),
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES)

    def __str__(self):
        return self.role


class FFXIVClass(models.Model):
    lore = models.TextField(null=True)
    name = models.CharField(max_length=200, null=False)
    dng_role = models.ForeignKey('RoleSelect')
    icon = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()


    def __str__(self):
        return self.name
        return self.lore
        return selficon
