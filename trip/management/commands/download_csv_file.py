from django.core.management.base import BaseCommand
import urllib.request
import os
import zipfile
import csv
from trip.models import Trip
import shutil


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url_file = input("Enter URL file :")
        # urllib.request.urlretrieve("https://s3.amazonaws.com/tripdata/201306-citibike-tripdata.zip", "201306-citibike-tripdata.zip")
        # for res in os.listdir():
        #     if res.split(".")[-1] == "zip":
        #         with zipfile.ZipFile(res, "r") as zip_ref:
        #             zip_ref.extractall("extract_file")
        #             dir_path = os.path.dirname(os.path.realpath(__file__)).replace("trip/management/commands","")
        #             with open(f"{dir_path}extract_file/{os.listdir(dir_path+'/extract_file')[0]}", 'r') as file:
        #                 reader = csv.reader(file)
        #                 counter = 1
        #                 for row in reader:
        #                     if counter > 1:
        #                         if row[13] == "NULL":
        #                             birth_date = None
        #                         else:
        #                             birth_date = row[13]
        #                         Trip.objects.create(
        #                             tripduration        = row[0],
        #                             start_time          = row[1],
        #                             stop_time           = row[2],
        #                             start_station_id    = row[3],
        #                             start_station_name  = row[4],
        #                             start_station_latitude = row[5],
        #                             start_station_longitude = row[6],
        #                             end_station_id      = row[7],
        #                             end_station_name    = row[8],
        #                             end_station_latitude= row[9],
        #                             end_station_longitude= row[10],
        #                             bike_id             = row[11],
        #                             user_type           = row[12],
        #                             birth_date          = birth_date,
        #                             gender              = row[14]
        #                         )
        #         os.unlink(res)
        #         shutil.rmtree(f"{dir_path}extract_file/", ignore_errors=True)



