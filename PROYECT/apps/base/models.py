from django.db import models

class BaseModel(models.Model):

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado', default = True)
    created_date = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)

    class Meta:
        
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'
