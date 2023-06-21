from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api_rest.serializers import UserSerializer, FormatSerializer, DownloadSerializer
from django.contrib.auth.models import User
from api_rest.models import Format, Download

class UserApiView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class FormatApiView(viewsets.ModelViewSet):
    queryset = Format.objects.all().order_by('id')
    serializer_class = FormatSerializer
    permission_classes = [permissions.IsAuthenticated]

class DownloadSerializer(viewsets.ModelViewSet):
    queryset = Download.objects.all().order_by('-id')
    serializer_class = DownloadSerializer
    permission_classes = [permissions.IsAuthenticated]