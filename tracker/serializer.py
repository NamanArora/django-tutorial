from rest_framework import serializers
from .models import Location

class Converter(serializers.ModelSerializer):
    class Meta:
        model= Location
        fields = ('longitude', 'latitude')