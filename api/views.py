from rest_framework.response import Response
from trip.models import Trip
from rest_framework import viewsets
from api.serializers import TripListSerializer
from rest_framework.pagination import PageNumberPagination
import requests
import geopy.distance
from rest_framework import status


success = {'code':status.HTTP_200_OK,'message':'success'}
no_argument = {'code':status.HTTP_400_BAD_REQUEST,'message':'no required parameter found'}
failed = {'code':status.HTTP_400_BAD_REQUEST,'message':'failed'}

class TripList(viewsets.ViewSet):
    def list(self , request):
        page_no = request.GET.get("page_no",10)
        paginator = PageNumberPagination()
        trip_obj = Trip.objects.all()
        paginator.page_size = page_no
        result_page = paginator.paginate_queryset(trip_obj, request)
        context = {
        "Message": success,
        "Output": TripListSerializer(result_page,many=True, context={'request': request}).data,
        }
        return Response(context)



class GetTripDetails(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        trip_id = data['trip_id']
        trip_obj = Trip.objects.get(id=trip_id)
        response = requests.get(f"https://api.weather.gov/points/{trip_obj.start_station_latitude},{trip_obj.start_station_longitude}").json()
        forecast = response['properties']['forecast']
        observation_stations_data = response['properties']['observationStations']
        weather_data_response = requests.get(forecast).json()
        observation_stations = requests.get(observation_stations_data).json()
        output = []
        for res in observation_stations['features']:
            output.append(res)
            for res in output:
                coordinates = res.get("geometry")
                coordinates = coordinates['coordinates']
                longitude = coordinates[1]
                latitude = coordinates[0]
                properties = res.get("properties")
                city_name = properties['name']
                coords_1 = (trip_obj.start_station_latitude , trip_obj.start_station_longitude)
                coords_2 = (longitude,latitude)
                nearest_city_distance = str(geopy.distance.geodesic(coords_1, coords_2).km).split(".")[0]
                nearest_location = {}
                nearest_location["City"] = city_name
                nearest_location["Distance"] = nearest_city_distance +" KM"
                break
            break
        context = {
            "Message": success,
            "Trip_Obj": TripListSerializer(trip_obj, many=False, context={'request': request}).data,
            "Nearest_Location":nearest_location,
            "Weather":weather_data_response['properties']['periods'][0]
        }
        return Response(context)

