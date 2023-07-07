from django.contrib import admin
from django.urls import path, include

from client.views import *

urlpatterns = [
    path('', download, name='download'),
]
