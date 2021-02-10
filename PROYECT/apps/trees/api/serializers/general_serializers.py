from apps.trees.models import TreeFamily
from rest_framework import serializers 

class TreeFamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = TreeFamily
        # Data filter:
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
