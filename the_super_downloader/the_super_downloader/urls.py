from django.contrib import admin
from django.urls import path, include

import client.urls as client_urls

urlpatterns = [
    path('', include(client_urls)),
    path('admin/', admin.site.urls),
]
