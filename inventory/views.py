from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CarSerializer, TruckSerializer, BoatSerializer
from .models import Car, Truck, Boat


class CarViewSet(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class TruckViewSet(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class TruckDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class BoatViewSet(generics.ListCreateAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer


class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boat.objects.all()
    serializer_class = BoatSerializer
