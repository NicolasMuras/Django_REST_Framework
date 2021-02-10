from apps.trees.models import Tree

from rest_framework import serializers

class TreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tree
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
