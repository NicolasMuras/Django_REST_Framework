from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from simple_history.models import HistoricalRecords

class ShroomManager(models.Manager):

    def create_shroom(self, specie, days, cap_color, trunk_color, password, **extra_fields):
        shroom = self.model(
            specie = specie,
            days = days,
            cap_color = cap_color,
            trunk_color = trunk_color
        )
        shroom.set_password(password)
        shroom.save(using=self.db)
        return shroom

class Shroom(AbstractBaseUser, models.Model):
    specie = models.CharField(max_length = 50)
    days = models.SmallIntegerField()
    cap_color = models.CharField(max_length=20, blank = False)
    trunk_color = models.CharField(max_length=20, blank = False)
    password = models.CharField(max_length=10, unique = True, blank = False, null = False)
    historical = HistoricalRecords()
    objects = ShroomManager()

    class Meta:
        verbose_name = 'Specie'
        verbose_name_plural = 'Species'

    def natural_key(self):
        return (self.specie)


    def __str__(self):
        return f'{self.specie}'