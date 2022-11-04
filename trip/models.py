from django.db import models

class Trip(models.Model):
    tripduration                   = models.CharField(max_length = 1000, null = True , blank = True)
    start_time                     = models.CharField(max_length = 1000,null = True , blank = True)
    stop_time                      = models.CharField(max_length = 1000 , blank = True)
    start_station_id               = models.CharField(max_length = 1000 ,null = True , blank = True)
    start_station_name             = models.CharField(max_length = 500 , null = True , blank = True)
    start_station_latitude         = models.CharField(max_length = 500 ,null = True , blank = True)
    start_station_longitude        = models.CharField(max_length = 500 ,null = True , blank = True)
    end_station_id                 = models.CharField(max_length = 500 ,null  = True , blank = True)
    end_station_name               = models.CharField(max_length = 500 , null = True , blank = True)
    end_station_latitude           = models.CharField(max_length = 500 ,null=True, blank=True)
    end_station_longitude          = models.CharField(max_length = 500 ,null=True, blank=True)
    bike_id                        = models.CharField(max_length = 500 ,null  = True , blank = True)
    user_type                      = models.CharField(max_length = 100 , null = True , blank = True)
    birth_date                     = models.CharField(max_length = 500 ,null = True , blank = True)
    gender                         = models.CharField(max_length = 100 , null = True , blank = True)

