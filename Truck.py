
class Truck:

   def __init__(self, truck_number):
       self.__number = truck_number
       self.__deliveries = []
       self.__current_capacity = 0

   def set_number(self, new_number):
       self.__number = new_number

   def set_deliveries(self, new_deliveries):
       self.__deliveries = (new_deliveries)

   def set_current_capacity(self, new_capacity):
       self.__current_capacity = new_capacity

   def get_number(self):
       return self.__number

   def get_deliveries(self):
       return self.__deliveries

   def get_current_capacity(self):
       return self.__current_capacity

   def add_delivery(self,new_delivery):
       self.__deliveries.append(new_delivery)

   def add_capacity(self, add):
       self.__current_capacity += add
