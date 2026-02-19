# Create a Python class called Vehicle with attributes for
# make, model, and year. Create two subclasses: Car
# (adds trunk size attribute) and Truck (adds payload
# capacity attribute). Each subclass should implement a
# method to display complete vehicle details.

class Vehicle :
    def __init__(self,make,model,year):
        self.MAKE = make
        self.MODEL = model
        self.YEAR = year

    def display(self):
        return self.MAKE,self.MODEL,self.YEAR

class Car(Vehicle):
    def __init__(self,make,model,year,trunk_size):
        super().__init__(make,model,year)
        self.TRUNK_SIZE = trunk_size

    def display(self):
        print('The Details about the car is :',super().display(),self.TRUNK_SIZE)
        
class Truck(Vehicle):
    def __init__(self,make,model,year,payload_capacity):
        super().__init__(make,model,year)
        self.PAYLOAD_CAPACITY = payload_capacity

    def display(self):
        print('The Details about the truck is :',super().display(),self.PAYLOAD_CAPACITY)

s1 = Car('Honda','Civic',2020,'15 cubic feet')
s2 = Truck('Ford','F-150',2021,'5000 lbs')
s1.display()
s2.display()