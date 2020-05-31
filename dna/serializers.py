from rest_framework import serializers
from .models import Dna


class DnaSerializer(serializers.ModelSerializer):
    """
    Geneneral purpose Dna Serializer
    """

    class Meta:
        model = Dna
        fields = ['dna']