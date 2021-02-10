from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class TreeFamily(BaseModel):

    # TODO: Define fields here
    description = models.CharField('Description', max_length=50, unique = True, null = False, blank = False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

     verbose_name = 'Tree Family'
     verbose_name_plural = 'Tree Families'

    def __str__(self):
        return self.description

class DamageIndicator(BaseModel):

    # TODO: Define fields here
    damage_indicator = models.PositiveSmallIntegerField(default = 0)
    tree_family = models.ForeignKey(TreeFamily, on_delete=models.CASCADE, verbose_name = 'Family Indicator')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

     verbose_name = 'Damage indicator'
     verbose_name_plural = 'Damage indicators'

    def __str__(self):

        return f'Damage Indicator {self.tree_family} : {self.damage_indicator}%'

class Tree(BaseModel):
    # TODO: Define fields here
    name = models.CharField('Especie del arbol', max_length=150, unique = True, blank = False, null = False)
    description = models.TextField('Descripcion del arbol', blank = False, null = False)
    image = models.ImageField('Imagen del arbol', upload_to='trees/', blank = True, null = True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:

     verbose_name = 'Tree Specie'
     verbose_name_plural = 'Tree Species'

    def __str__(self):

        return self.name