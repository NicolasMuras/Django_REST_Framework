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

class Tree(BaseModel):
    # TODO: Define fields here
    name = models.CharField('Especie del arbol', max_length=150, unique = True, blank = False, null = False)
    description = models.TextField('Descripcion del arbol', blank = False, null = False)
    tree_family = models.ForeignKey(TreeFamily, on_delete=models.CASCADE, verbose_name = 'Familia', null = True)
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