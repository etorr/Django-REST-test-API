from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from faker import Faker


class TestSetup(APITestCase):
    def setUp(self):
        self.jwt_url = reverse("token_obtain_pair")
        self.jwt_refresh_url = reverse("token_refresh")
        self.fake = Faker()

        self.username = self.fake.user_name()
        self.email = self.fake.email()
        self.password = self.fake.password()

        self.user_data = {
            "username": self.username,
            "password": self.password,
        }

        self.u = User.objects.create_user(
            self.username, self.email, self.password)
        self.u.is_active = True
        self.u.save()

        self.car_data = {
            "make": "Honda",
            "model": "Civic",
            "year": "1990",
            "seats": "5",
            "color": "red",
            "vin": "adf5a7dda75fa75da75",
            "current_mileage": "79000",
            "service_interval": "4000",
            "next_service": "81000"
        }

        self.truck_data = {
            "make": "Chevrolet",
            "model": "Silverado",
            "year": "1992",
            "bed_length": "8",
            "seats": "3",
            "color": "Burgandy",
            "vin": "adsfads87adsfadf787",
            "current_mileage": "288000",
            "service_interval": "3000",
            "next_service": "291000"
        }

        self.boat_data = {
            "make": "Boat Brand",
            "model": "boaty",
            "year": "1990",
            "length": "45",
            "width": "20",
            "hin": "adf76ad785ad85ad87f5",
            "current_hours": "79000",
            "service_interval": "4000",
            "next_service": "81000"
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
