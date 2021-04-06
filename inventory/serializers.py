from rest_framework import serializers
from .models import Car, Truck, Boat


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'seats', 'color', 'vin',
                  'current_mileage', 'service_interval', 'next_service')


class TruckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Truck
        fields = ('make', 'model', 'year', 'seats', 'bed_length', 'color',
                  'vin', 'current_mileage', 'service_interval', 'next_service')


class BoatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boat
        fields = ('make', 'model', 'year', 'length', 'width', 'hin',
                  'current_hours', 'service_interval', 'next_service')
