# Create base class Cab with cabnumber,drivername and
# base fare.Create subclasses Minicab, sedancab and
# Luxury cab.Each subclass should override
# calculate_fare(distance) with different per km rates.
from datetime import datetime
class Cab :
    service_history = {}
    base_fare = 100
    cab_number = 1000
    def __init__(self,driver_name):
        self.CAB_NUMBER = Cab.cab_number
        self.DRIVER_NAME = driver_name
        Cab.cab_number += 1
        self.TIMEPERIOD = datetime.now()
    def __str__(self):
        return f"{self.TIMEPERIOD}|Cab Number:{self.cab_number}|Driver Name:{self.DRIVER_NAME}"

    def calculate_fare(self,distance,per_km_rates):
        fare = self.base_fare+(distance * per_km_rates)
        return fare

class MiniCab(Cab):
    driver_name = "Malhar"
    rate = 60
    
    def __init__(self,distance):
        super().__init__(MiniCab.driver_name)
        self.DISTANCE = distance
        self.RATE = MiniCab.rate
    
    def __str__(self):
        return super().__str__()+f"|DistanceL:{self.DISTANCE}|Rate/km:{self.RATE}|Total Fare:{self.calculate_fare(self.DISTANCE,self.RATE)}"


class SedanCab(Cab):
    
    driver_name="Smit"
    rate = 120
    
    def __init__(self,distance):
        super().__init__(SedanCab.driver_name)
        self.DISTANCE = distance
        self.RATE = SedanCab.rate
    
    def __str__(self):
        return super().__str__()+f"|DistanceL:{self.DISTANCE}|Rate/km:{self.RATE}|Total Fare:{self.calculate_fare(self.DISTANCE,self.RATE)}"
    

class LuxuryCab(Cab):
    
    Driver_name="Rahul"
    rate = 240
    
    def __init__(self,distance):
        super().__init__(LuxuryCab.Driver_name)
        self.DISTANCE = distance
        self.RATE = LuxuryCab.rate
    
    def __str__(self):
        return super().__str__()+f"|DistanceL:{self.DISTANCE}|Rate/km:{self.RATE}|Total Fare:{self.calculate_fare(self.DISTANCE,self.RATE)}"
    
# c1 = MiniCab(10,'abc',12,60)
# c1.display()

# c2 = SedanCab(20,'def',10,80)
# c2.display()

# c1 = LuxuryCab(30,'ghi',5,100)
# c1.display()

class main(MiniCab , SedanCab,LuxuryCab):
    while True:
        print('\n=====================================')
        print('Welcome to the Cab Service Dashboard')
        print('Please choose from the below given options (base price : ₹100 will be added.):')
        print('1.Order a Minicab Service')
        print('2.Order a Sedancab Service')
        print('3.Order a Luxurycab Service')
        print('4.Show Service History')
        print('5.Exit')
        print('=======================================')

        choice = int(input('Enter the choice here :'))

        if choice == 1:
            print('\n=====================================')
            print('Thank You for choosing MiniCab Service.!(Minicab rate:\'₹60perKM\' will charge separately..)')
            distance = int(input('Please The distance for which you will be using our cab service (in km):'))
            service = MiniCab(distance)
            MiniCab.service_history[service.CAB_NUMBER] = service
            print('\n',service,'\n')
            print('Thank you for using our Cab Service.\n')
        elif choice == 2 :
            print('\n=====================================')
            print('Thank You for choosing SedanCab Service.!(Sedancab rate:\'₹120perKM\' will charge separately..)')
            distance = int(input('Please The distance for which you will be using our cab service (in km):'))
            service = SedanCab(distance)
            SedanCab.service_history[service.CAB_NUMBER] = service
            print('\n',service,'\n')
            print('Thank you for using our Cab Service.\n')
        elif choice == 3 :
            print('\n=====================================')
            print('Thank You for choosing LuxuryCab Service.!(Luxurycab rate:\'₹240perKM\' will charge separately..)')
            distance = int(input('Please The distance for which you will be using our cab service (in km):'))
            service = LuxuryCab(distance)
            LuxuryCab.service_history[service.CAB_NUMBER] = service
            print('\n',service,'\n')
            print('Thank you for using our Cab Service.\n')
        elif choice == 4 :
            print('\n=====================================')
            print('Gathering the data:\n')
            services = Cab.service_history
            for i in services :
                print(services.get(i))
            print('\nThank you for using our Cab Service.\n')
        elif choice == 5:
            print('\n=====================================')
            print('Exiting the Cab Service Dashboard.')
            print('Thank you for using our Cab Service.')
            print('And Visit Again.!\n')
            break
        else:
            print('\nInvalid Choice.Please enter a valid choice.\n')
