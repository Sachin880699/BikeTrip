from trip.models import *
from rest_framework import serializers


class TripListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'