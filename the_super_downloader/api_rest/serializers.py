from django.contrib.auth.models import User
from api_rest.models import Format, Download
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['__all__']


class FormatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Format
        fields = ['__all__']

class DownloadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Download
        fields = ['__all__']