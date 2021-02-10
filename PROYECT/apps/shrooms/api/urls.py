from django.urls import path
from apps.shrooms.api.api import shroom_api_view, shroom_detail_api_view

urlpatterns = [
    path('shroom/', shroom_api_view, name = 'shroom_api'),
    path('shroom/<int:pk>', shroom_detail_api_view, name = 'shroom_detail_api_view')
]