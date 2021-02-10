from django.urls import path
from apps.trees.api.views.general_views import TreeFamilyListAPIView

urlpatterns = [
    path('tree_family/', TreeFamilyListAPIView.as_view(), name = 'tree_family')
]

