from django.db import models

class Shroom(models.Model):
    specie = models.CharField(max_length = 50)
    days = models.SmallIntegerField()
    cap_color = models.CharField(max_length=20, blank = False)
    trunk_color = models.CharField(max_length=20, blank = False)
    secret = models.CharField(max_length=10, unique = True, blank = False, null = False)

    class Meta:
        verbose_name = 'Specimen'
        verbose_name_plural = 'Specimens'

    def __str__(self):
        return f'{self.specie}'