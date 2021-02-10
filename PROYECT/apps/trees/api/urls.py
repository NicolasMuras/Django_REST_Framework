from django.urls import path
from apps.trees.api.views.general_views import TreeFamilyListAPIView
from apps.trees.api.views.tree_views import TreeListAPIView

urlpatterns = [
    path('tree_family/', TreeFamilyListAPIView.as_view(), name = 'tree_family'),
    path('tree/', TreeListAPIView.as_view(), name = 'tree')
]

