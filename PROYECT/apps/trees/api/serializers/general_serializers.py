from apps.trees.models import FamilyTree, DamageIndicator
from rest_framework import serializers 

class FamilyTreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FamilyTree
        exclude = ('estate',)

class DamageIndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = DamageIndicator
        exclude = ('state',)