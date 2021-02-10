from apps.trees.models import Tree

from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tree
        exclude = ('state',)
