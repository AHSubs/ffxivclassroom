from django.db import models
from django.utils import timezone

# Create your models here.

class BaseClass (models.Model):
    cname = (
        ('Gladiator','GLA'),
        ('Marauder','MRD'),
        ('Pugilist','PGL'),
        ('Lancer','LNC'),
        ('Archer','ARC'),
        ('Rogue','ROG'),
        ('Conjurer','CNJ'),
        ('Thaumaturge','THM'),
        ('Arcanist','ACN'),
        ('Nessuno','-'),
    )
    baseclassname = models.CharField(max_length=40,choices=cname,verbose_name='Elenco Classi Base')

    class Meta:
        verbose_name_plural = "Elenco Classi (Base)"
        verbose_name = "Elenco Classe (Base)"

    def __str__(self):
        return self.baseclassname

class BaseJob (models.Model):
    jname = (
        ('Paladin','PLD'),
        ('Warrior','WAR'),
        ('Dark Knight','DRK'),
        ('Monk','MNK'),
        ('Dragoon','DRG'),
        ('Bard','BRD'),
        ('Machinist','MCH'),
        ('Ninja','NIN'),
        ('White Mage','WHM'),
        ('Black Mage','BLM'),
        ('Scholar','SCH'),
        ('Summoner','SMN'),
        ('Astrologian','AST'),
    )
    basejobname = models.CharField(max_length=40,choices=jname,verbose_name='Nome del Job')

    class Meta:
        verbose_name ="Elenco Job"
        verbose_name_plural="Elenco Jobs"

    def __str__(self):
        return self.basejobname

class Role (models.Model):

    roles = (
        ('TANK','Tank'),
        ('DPS','Dps'),
        ('HEALER','Healer'),

    )
    rolename = models.CharField(max_length=10,choices=roles,verbose_name='Nome Ruolo')

    class Meta:
        verbose_name_plural = "Ruolo"
        verbose_name = "Ruolo"

    def __str__(self):
        return self.rolename

class Expansion (models.Model):
    exp = (
        ('A Realm Reborn','ARR'),
        ('Heavensward','HW'),
    )
    expname = models.CharField(max_length=20,choices=exp,verbose_name="Espansione Di Uscita")

    class Meta:
        verbose_name = "Espansione"
        verbose_name_plural = "Espansioni"

    def __str__(self):
        return self.expname

class Level(models.Model):
    lvl = (
          ('15','15'),
          ('30','30'),
          ('-','-'),
    )
    lvllist = models.CharField(max_length=2,choices=lvl,verbose_name="Livello")

    class Meta:
        verbose_name_plural ="Livelli"
        verbose_name = "Livello"

    def __str__(self):
        return self.lvllist

class Stat (models.Model):

    stats = (
        ('Vitality','VIT'),
        ('Strength','STR'),
        ('Dexterity','DEX'),
        ('Intelligence','INT'),
        ('Mind','Mind'),
        ('Piety','PIE'),
    )
    statsname = models.CharField(max_length=30,choices=stats,verbose_name="Nome Statistica")

    class Meta:
        verbose_name_plural = "Statistiche"
        verbose_name = "Statistica"

    def __str__(self):
        return self.statsname

class Base (models.Model):
    name = models.ForeignKey('BaseClass',verbose_name="Nome Classe")
    role = models.ForeignKey('Role',verbose_name="Ruolo")
    avail = models.ForeignKey('Expansion',verbose_name="Espansione di Uscita")
    lore = models.TextField(blank=True,verbose_name="Lore")
    transformin = models.ForeignKey('BaseJob',verbose_name="Trasformazione in Job")
    trasforminjobat = models.ForeignKey('Level',verbose_name="Trasformazione in Job al livello")
    icon = models.CharField(null=True,max_length=255,verbose_name="Icona Classe / Job")
    creat_date = models.DateTimeField(default=timezone.now,verbose_name="Data di Creazione")
    pub_date = models.DateTimeField(blank=True,null=True,verbose_name="Data di Pubblicazione")
    stat = models.ForeignKey('Stat',verbose_name="Statistica Primaria",null=True)

    class Meta:
        verbose_name = "Classe Base"
        verbose_name_plural = "Classi Base"

    def __str__(self):
        return self.icon

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

class Job (models.Model):
    name = models.ForeignKey('BaseJob',verbose_name="Nome Job")
    role = models.ForeignKey('Role',verbose_name="Ruolo")
    avail = models.ForeignKey('Expansion',verbose_name="Espansione di Uscita")
    lore = models.TextField(blank=True,verbose_name="Lore JOB")
    transfrom1 = models.ForeignKey('BaseClass',verbose_name="Nome Classe 1",related_name="transfrom1",null=True)
    transfrom2 = models.ForeignKey('BaseClass',verbose_name="Nome Classe 2",related_name="transfrom2",null=True)
    transfromlvl1 = models.ForeignKey('Level',verbose_name="Livello 1",related_name="transfromlvl1",null=True)
    transfromlvl2 = models.ForeignKey('Level',verbose_name="Livello 2",related_name="transfromlvl2",null=True)
    icon = models.CharField (verbose_name="Icona JOB",null=True,blank=True,max_length=255)
    creat_date = models.DateTimeField(default=timezone.now, verbose_name="Data di Creazione")
    pub_date = models.DateTimeField(blank=True, null=True, verbose_name="Data di Pubblicazione")
    stat = models.ForeignKey('Stat', verbose_name="Statistica Primaria", null=True)

    class Meta:
        verbose_name = "Job"
        verbose_name_plural ="Jobs"

    def __str__(self):
        return self.icon

    def publish(self):
        self.pub_date = timezone.now()
        self.save()