
from geopy.geocoders import Nominatim
import pandas as pd
geolocator = Nominatim(user_agent='your_app_name')


import math

class Delivery:

   def __init__(self, address):
       self.__address = address
       # __latitude = api to nominatim sending in address
       self.__latitude = 0
       # __longitude = api to nominatim sending in address
       self.__longitude = 0
       self.__num_small_packages = 0
       self.__num_medium_packages = 0
       self.__num_big_packages = 0


   def set_address(self, new_address):
       self.__address = new_address

   def set_longitude(self, new_longitude):
       self.__longitude = new_longitude

   def set_latitude(self, new_latitude):
       self.__latitude = (new_latitude)

   def set_num_small_packages(self, new_num_small_packages):
       self.__num_small_packages = new_num_small_packages

   def set_num_medium_packages(self, new_num_medium_packages):
       self.__num_medium_packages = new_num_medium_packages

   def set_num_big_packages(self, new_num_big_packages):
       self.__num_big_packages = new_num_big_packages

   def get_address(self):
       return self.__address

   def get_longitude(self):
       return self.__longitude

   def get_latitude(self):
       return self.__latitude

   def get_num_small_packages(self):
       return self.__num_small_packages

   def get_num_medium_packages(self):
       return self.__num_medium_packages

   def get_num_big_packages(self):
       return self.__num_big_packages

   def get_total_units(self):
       SMALL_SIZE = 2
       MEDIUM_SIZE = 4
       LARGE_SIZE = 8
       units = self.__num_small_packages * SMALL_SIZE + self.__num_medium_packages * MEDIUM_SIZE + self.__num_big_packages * LARGE_SIZE
       return units

   def find_distance(self, other_longitude, other_latitude):
       distance = math.abs(other_latitude + other_longitude - self.__getlatitude()-self.__getlongitude())
       return distance

   def find_long_and_lat(self):
       house = self.__address
       df2 = pd.DataFrame({'Location':
                               [house]})

       df2[['location_lat', 'location_long']] = df2['Location'].apply(
           geolocator.geocode).apply(lambda x: pd.Series(
           [x.latitude, x.longitude], index=['location_lat', 'location_long']))


       point = (df2[['location_lat', 'location_long']])
       lat = df2.loc[0, 'location_lat']
       long = df2.loc[0, 'location_long']


