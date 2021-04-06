from .test_setup import TestSetup
from ..models import *
from model_bakery import baker


class TestModel(TestSetup):
    def test_car_model(self):
        car = baker.make(Car, vin="asdf56dsf765dfdfd7d")
        self.assertEqual(str(car), "asdf56dsf765dfdfd7d")

    def test_truck_model(self):
        truck = baker.make(Truck, vin="adsg76dg5dg7dgdg")
        self.assertEqual(str(truck), "adsg76dg5dg7dgdg")

    def test_boat_model(self):
        boat = baker.make(Boat, hin="dgadsftads765a87dsf5")
        self.assertEqual(str(boat), "dgadsftads765a87dsf5")
