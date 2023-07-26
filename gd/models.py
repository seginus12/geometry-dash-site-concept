from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=20, decimal_places=2)
    current_rank = models.IntegerField()
    max_rank = models.IntegerField()
    registration_date = models.DateField("Registation date")

class Level(models.Model):
    # level id
    title = models.CharField(max_length=50)
    length = models.DurationField()
    creator = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    status = models.CharField("On of several statuses", max_length=50) # выбор из нескольких опций
    publication_time = models.DateTimeField()
    music = models.URLField(max_length=200)

# class progress
    # progress
    # Player
    # Level