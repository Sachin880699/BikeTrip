from django.db import models

class Trip(models.Model):
    tripduration                   = models.CharField(max_length = 1000, null = True , blank = True)
    start_time                     = models.DateTimeField(null = True , blank = True)
    stop_time                      = models.DateTimeField(blank = True , null = True)
    start_station_id               = models.IntegerField(null = True , blank = True)
    start_station_name             = models.CharField(max_length = 500 , null = True , blank = True)
    start_station_latitude         = models.FloatField(null = True , blank = True)
    start_station_longitude        = models.FloatField(null = True , blank = True)
    end_station_id                 = models.IntegerField(null  = True , blank = True)
    end_station_name               = models.CharField(max_length = 500 , null = True , blank = True)
    end_station_latitude           = models.FloatField(null=True, blank=True)
    end_station_longitude          = models.FloatField(null=True, blank=True)
    bike_id                        = models.IntegerField(null  = True , blank = True)
    user_type                      = models.CharField(max_length = 100 , null = True , blank = True)
    birth_date                     = models.IntegerField(null = True , blank = True)
    gender                         = models.IntegerField(null = True , blank = True)

    def __str__(self):
        return self.start_station_name


