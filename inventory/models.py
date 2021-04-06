from django.db import models


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=50, null=False)
    model = models.CharField(max_length=50, null=False)
    year = models.IntegerField(null=False)
    seats = models.IntegerField(null=False)
    color = models.CharField(max_length=50, null=False)
    vin = models.CharField(max_length=50, null=False)
    current_mileage = models.IntegerField(null=False)
    service_interval = models.IntegerField(null=False)
    next_service = models.IntegerField(null=False)

    def __str__(self):
        return self.vin


class Truck(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=50, null=False)
    model = models.CharField(max_length=50, null=False)
    year = models.IntegerField(null=False)
    seats = models.IntegerField(null=False)
    bed_length = models.IntegerField(null=False)
    color = models.CharField(max_length=50, null=False)
    vin = models.CharField(max_length=50, null=False)
    current_mileage = models.IntegerField(null=False)
    service_interval = models.IntegerField(null=False)
    next_service = models.IntegerField(null=False)

    def __str__(self):
        return self.vin


class Boat(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=50, null=False)
    model = models.CharField(max_length=50, null=False)
    year = models.IntegerField(null=False)
    length = models.IntegerField(null=False)
    width = models.IntegerField(null=False)
    hin = models.CharField(max_length=50, null=False)
    current_hours = models.IntegerField(null=False)
    service_interval = models.IntegerField(null=False)
    next_service = models.IntegerField(null=False)

    def __str__(self):
        return self.hin
