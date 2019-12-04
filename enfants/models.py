from django.db import models

class Handicaps(models.Model):
    handicap_id = models.AutoField(primary_key=True)
    nom_handicap = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class Enfants(models.Model):
    enfant_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    handicap = models.ForeignKey(Handicaps, related_name='handicaps', on_delete = models.CASCADE)