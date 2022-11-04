from rest_framework import routers
from django.urls import re_path as url , include
from api.views import TripList , GetTripDetails

router = routers.DefaultRouter()

router.register(r'trip_list', TripList, basename='trip_list')
router.register(r'trip_details', GetTripDetails, basename='trip_details')

urlpatterns = [
        url(r'^', include(router.urls)),
]