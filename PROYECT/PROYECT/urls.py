from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shroom/', include('apps.shrooms.api.urls')),
    path('trees/', include('apps.trees.api.urls'))
]
