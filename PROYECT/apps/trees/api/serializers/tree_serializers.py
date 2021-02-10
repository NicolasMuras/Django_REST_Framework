from rest_framework import serializers
from apps.trees.models import Tree
from apps.trees.api.serializers.general_serializers import TreeFamilySerializer

class TreeSerializer(serializers.ModelSerializer):
    # Show foreign key value, method 1:
    # tree_family = TreeFamilySerializer()

    # Show foreign key value, method 2:
    #tree_family = serializers.StringRelatedField()

    class Meta:
        model = Tree
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'tree_family': instance.tree_family.description
        }
