from django.urls import path, include
from .views import *

urlpatterns = [
    path('cars/', CarViewSet.as_view(), name='cars-all'),
    path('trucks/', TruckViewSet.as_view(), name='trucks-all'),
    path('boats/', BoatViewSet.as_view(), name='boats-all'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='cars-detail'),
    path('trucks/<int:pk>/', TruckDetail.as_view(), name='trucks-detail'),
    path('boats/<int:pk>/', BoatDetail.as_view(), name='boats-detail'),
]
