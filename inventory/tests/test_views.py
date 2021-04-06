from .test_setup import TestSetup
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers import *


class TestView(TestSetup):
    def test_user_cannot_obtain_jwt_token_pair_with_no_data(self):
        res = self.client.post(self.jwt_url)

        # JWT token without credentials should not be allowed
        self.assertEqual(res.status_code, 400)

    def test_user_can_obtain_jwt_token_pair(self):
        res = self.client.post(
            self.jwt_url, self.user_data, format='json')

        self.assertEqual(res.status_code, 200)

    def test_user_cannot_obtain_jwt_token_pair_with_incorrect_data(self):
        res = self.client.post(
            self.jwt_url, data={"username": "wrongusername", "password": "wrongpassword"}, format='json')
        self.assertEqual(res.status_code, 401)

    def test_list_cars(self):
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        res = self.client.get('/cars/', data={'format': 'json'})
        self.assertEqual(res.status_code, 200)

    def test_read_create_car(self):
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        res1 = self.client.post('/cars/', self.car_data, format='json')
        self.assertEqual(res1.status_code, 201)
        res = self.client.get('/cars/1/', format='json')
        self.assertEqual(res.status_code, 200)

    def test_update_car_data(self):
        update_car_data = {
            "make": "Honda",
            "model": "Civic",
            "year": "1992",
            "seats": "5",
            "color": "red",
            "vin": "adf5a7dda75fa75da75",
            "current_mileage": "78000",
            "service_interval": "4000",
            "next_service": "80000"
        }
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.client.post('/cars/', self.car_data, format='json')
        res = self.client.put(
            '/cars/1/', update_car_data, format='json')
        serializer = CarSerializer(update_car_data)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, 200)

    def test_delete_car(self):
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.client.post('/cars/', self.car_data, format='json')
        res = self.client.delete('/cars/1/')
        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, 204)

    def test_list_trucks(self):
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        res = self.client.get('/trucks/', data={'format': 'json'})
        self.assertEqual(res.status_code, 200)

    def test_read_create_truck(self):
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        res1 = self.client.post('/trucks/', self.truck_data, format='json')
        self.assertEqual(res1.status_code, 201)
        res = self.client.get('/trucks/1/', format='json')
        self.assertEqual(res.status_code, 200)

    def test_update_truck_data(self):
        update_truck_data = {
            "make": "Chevrolet",
            "model": "Silverado",
            "year": "2007",
            "seats": "3",
            "bed_length": "12",
            "color": "Burgandy",
            "vin": "adf5a7dda75fa75da75",
            "current_mileage": "78000",
            "service_interval": "4000",
            "next_service": "80000"
        }
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.client.post('/trucks/', self.truck_data, format='json')
        res = self.client.put(
            '/trucks/1/', update_truck_data, format='json')
        serializer = TruckSerializer(update_truck_data)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, 200)

    def test_delete_truck(self):
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.client.post('/trucks/', self.truck_data, format='json')
        res = self.client.delete('/trucks/1/')
        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, 204)

    def test_list_boat(self):
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        res = self.client.get('/boats/', data={'format': 'json'})
        self.assertEqual(res.status_code, 200)

    def test_read_create_boat(self):
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        res1 = self.client.post('/boats/', self.boat_data, format='json')
        self.assertEqual(res1.status_code, 201)
        res = self.client.get('/boats/1/', format='json')
        self.assertEqual(res.status_code, 200)

    def test_update_boat_data(self):
        update_boat_data = {
            "make": "Boater",
            "model": "Boatt",
            "year": "1959",
            "length": "43",
            "width": "21",
            "hin": "adf5a7dda75fa75da75",
            "current_hours": "78000",
            "service_interval": "4000",
            "next_service": "80000"
        }
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.client.post('/boats/', self.boat_data, format='json')
        res = self.client.put(
            '/boats/1/', update_boat_data, format='json')
        serializer = BoatSerializer(update_boat_data)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, 200)

    def test_delete_boat(self):
        refresh = RefreshToken.for_user(self.u)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        self.client.post('/boats/', self.boat_data, format='json')
        res = self.client.delete('/boats/1/')
        self.assertEqual(res.data, None)
        self.assertEqual(res.status_code, 204)
