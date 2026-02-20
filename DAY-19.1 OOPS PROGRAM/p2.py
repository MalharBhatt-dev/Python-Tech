# Create a Python class called Vehicle with attributes for
# make, model, and year. Create two subclasses: Car
# (adds trunk size attribute) and Truck (adds payload
# capacity attribute). Each subclass should implement a
# method to display complete vehicle details.

class Vehicle :
    
    vehicles = {}
    vehicle_id = 1000
    
    def __init__(self,make,model,year):
        Vehicle.vehicle_id += 1
        self.MAKE = make
        self.MODEL = model
        self.YEAR = year
        self.VEHICLE_ID = Vehicle.vehicle_id
        
    def __str__(self):
        return f"ID :{self.VEHICLE_ID} |Company :{self.MAKE} |Model :{self.MODEL} |Year :{self.YEAR}"
    
    def show_registered_vehicle(self,vehicleId):
        vehicle = Vehicle.vehicles.get(vehicleId)
        if not vehicle :
            print('Vehicle not found.')
            return False
        print(vehicle)

    def display(self):
        return self.MAKE,self.MODEL,self.YEAR

class Car(Vehicle):

    def __init__(self,make,model,year,trunk_size):
        super().__init__(make,model,year)
        self.TRUNK_SIZE = trunk_size
        super().vehicles[self.VEHICLE_ID] = self

    def __str__(self):
        return super().__str__()+f" |Trunksize :{self.TRUNK_SIZE}"
    
    def display(self):
        print('The Details about the car is :',super().display(),self.TRUNK_SIZE)
        
class Truck(Vehicle):
    
    def __init__(self,make,model,year,payload_capacity):
        super().__init__(make,model,year)
        self.PAYLOAD_CAPACITY = payload_capacity
        super().vehicles[self.VEHICLE_ID] = self

    def __str__(self):
        return super().__str__()+f" |Payload Capacity :{self.PAYLOAD_CAPACITY}"
    
    def display(self):
        print('The Details about the truck is :',super().display(),self.PAYLOAD_CAPACITY)

# s1 = Car('Honda','Civic',2020,'15 cubic feet')
# s2 = Truck('Ford','F-150',2021,'5000 lbs')
# s1.display()
# s2.display()

class main(Car,Truck):
    while True:
        print('\n===============================')
        print('Welcome to the Vehicle info CLI')
        print('Please choose the required option :')
        print('1.Car')
        print('2.Truck')
        print('3.Show Vehicle Details.')
        print('4.Exit')
        print('=================================')
        choice = int(input('Enter the choice here :'))

        if choice == 1:
            print('\nEntering Car Info Dashboard.')
            make = input('Enter the car company name :')
            model = input('Enter the model of the car :')
            year = int(input('Enter the year of the car in YYYY format :'))
            trunksize = int(input('Enter the trunksize of the car :'))
            Car(make,model,year,trunksize).display()

        elif choice == 2:
            print('\nEntering Truck Info Dashboard.')
            make = input('Enter the Truck company name :')
            model = input('Enter the model of the Truck :')
            year = int(input('Enter the year of the Truck in YYYY format :'))
            payload_capacity = int(input('Enter the payload capacity of the Truck :'))
            Truck(make,model,year,payload_capacity).display()
        
        elif choice == 3 :
            print('Showing the Required Details.')
            id = int(input('Enter the vehicle ID :'))
            Vehicle.show_registered_vehicle(Vehicle,id)

        elif choice == 4 :
            print('\nExiting The Vehicle Info Dashboard.')
            print('Thank You and Visit again.')
            break

        else :
            print('\nInvalid choice.Please enter a valid choice.')