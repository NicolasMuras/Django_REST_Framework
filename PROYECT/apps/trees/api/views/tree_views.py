from apps.base.api import GeneralListApiView
from apps.trees.api.serializers.tree_serializers import TreeSerializer

class TreeListAPIView(GeneralListApiView):
    serializer_class = TreeSerializer