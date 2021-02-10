from rest_framework import generics
from apps.trees.models import DamageIndicator, TreeFamily
from apps.trees.api.serializers.general_serializers import TreeFamilySerializer, DamageIndicatorSerializer

class TreeFamilyListAPIView(generics.ListAPIView):
    serializer_class = TreeFamilySerializer

    def get_queryset(self):
        return TreeFamily.objects.filter(state = True)
