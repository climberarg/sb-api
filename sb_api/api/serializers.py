from rest_framework import serializers
from .models import BackScratcher


# Serializers define the API representation.
class BackScratcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackScratcher
        fields = ('id', 'name', 'description', 'size', 'price')