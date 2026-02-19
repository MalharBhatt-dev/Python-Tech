# Create base class Cab with cabnumber,drivername and
# base fare.Create subclasses Minicab, sedancab and
# Luxury cab.Each subclass should override
# calculate_fare(distance) with different per km rates.

class Cab :
    base_fare = 100
    def __init__(self,cab_number,driver_name):
        self.CAB_NUMBER = cab_number
        self.DRIVER_NAME = driver_name

    def calculate_fare(self,distance,per_km_rates):
        fare = self.base_fare+(distance * per_km_rates)
        return fare

class MiniCab(Cab):
    def __init__(self,cab_number,driver_name,distance,rate):
        super().__init__(cab_number,driver_name)
        self.DISTANCE = distance
        self.RATE = rate
    
    def display(self):
        print('The total fare is',self.calculate_fare(self.DISTANCE,self.RATE))

class SedanCab(Cab):
    def __init__(self,cab_number,driver_name,distance,rate):
        super().__init__(cab_number,driver_name)
        self.DISTANCE = distance
        self.RATE = rate
    
    def display(self):
        print('The total fare is',self.calculate_fare(self.DISTANCE,self.RATE))

class LuxuryCab(Cab):
    def __init__(self,cab_number,driver_name,distance,rate):
        super().__init__(cab_number,driver_name)
        self.DISTANCE = distance
        self.RATE = rate
    
    def display(self):
        print('The total fare is',self.calculate_fare(self.DISTANCE,self.RATE))

c1 = MiniCab(10,'abc',12,60)
c1.display()

c2 = SedanCab(20,'def',10,80)
c2.display()

c1 = LuxuryCab(30,'ghi',5,100)
c1.display()
