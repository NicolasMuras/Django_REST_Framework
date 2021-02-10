from rest_framework import generics
from apps.base.api import GeneralListApiView
from apps.trees.api.serializers.general_serializers import TreeFamilySerializer

class TreeFamilyListAPIView(GeneralListApiView):
    serializer_class = TreeFamilySerializer
