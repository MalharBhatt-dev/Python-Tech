
#h Create a Python class called Building with attributes for
#h address, number of floors, and total area. Create two
#h subclasses: ResidentialBuilding (adds number of
#h apartments and rent per apartment) and
#h CommercialBuilding (adds office space area and rent per
#h square foot). Each subclass should include a method to
#h calculate total rent

class Building :
    
    buildings = {}
    sr_no = 1
    
    def __init__(self,address,noOfFloors,totalArea):
        self.SR_NO = Building.sr_no
        Building.sr_no += 1
        self.ADDRESS = address
        self.NO_OF_FLOORS = noOfFloors
        self.TOTAL_AREA = totalArea
    
    def __str__(self):
        return f"{self.SR_NO} |Building Address:{self.ADDRESS} |No.of floors:{self.NO_OF_FLOORS} |Total area:{self.TOTAL_AREA}"

class ResidentialBuilding(Building):
    
    def __init__(self,address,no_of_floors,total_area,no_of_apartments,rent_per_apartment):    
        super().__init__(address,no_of_floors,total_area)
        self.NO_OF_APARTMENTS = no_of_apartments
        self.RENT_PER_APARTMENT = rent_per_apartment
    
    def __str__(self):
        return super().__str__()+f"|No.of Apartments:{self.NO_OF_APARTMENTS} |rent per Apartment:₹{self.RENT_PER_APARTMENT} |Current Rent:₹{self.calculate_rent()}"
    
    def calculate_rent(self):
        rent_amt =  self.NO_OF_APARTMENTS * self.NO_OF_FLOORS*self.RENT_PER_APARTMENT 
        return rent_amt
            

class CommercialBuilding(Building):
    
    def __init__(self,address,no_of_floors,total_area,office_space_area,rent_per_square_foot):
        super().__init__(address,no_of_floors,total_area)
        self.OFFICE_SPACE_AREA = office_space_area
        self.RENT_PER_SQUARE_FOOT = rent_per_square_foot
    
    def __str__(self):
        return super().__str__()+f"|Office space area:{self.OFFICE_SPACE_AREA} |Rent per squarefoot:₹{self.RENT_PER_SQUARE_FOOT} |Current Rent:₹{self.calculate_rent()}"
    
    def calculate_rent(self):
        rent_amt = self.OFFICE_SPACE_AREA*self.RENT_PER_SQUARE_FOOT*self.NO_OF_FLOORS
        return rent_amt
     

# r1 = ResidentialBuilding("abc",3,2500,6,4500)
# r1.display()

# r2 = CommercialBuilding('def',5,2000,202,1200)
# r2.display()

class main(ResidentialBuilding,CommercialBuilding):
    while True:
        print('\n=====================================')
        print('Welcome to the Building Info Dashboard')
        print('Please choose from the below given options :')
        print('1.Add a Residential Property/Building')
        print('2.Add a Commercial Property/Building')
        print('3.Show Property with current rent.')
        print('4.Exit')
        print('=======================================')

        choice = int(input('Enter the choice here :'))

        if choice == 1:
            print('\nEntering Residential Building Registration.')
            address = input('Enter the Address of the building :')
            total_area = int(input('Enter the total area of the building (in sqft):'))
            no_of_floors = int(input('Enter the number of floors the building has :'))
            no_of_apartments = int(input('Enter the number of apartments per floor the building has :'))
            rent_per_apartment = int(input('Enter rent per apartment of the building :'))

            building = ResidentialBuilding(address,no_of_floors,total_area,no_of_apartments,rent_per_apartment)
            Building.buildings[building.SR_NO] = building

            if not building :
                print('Registration is Failed.')
        
        elif choice == 2:
            print('\nEntering Commercial Building Registration.')
            address = input('Enter the Address of the building :')
            total_area = int(input('Enter the total area of the building (in sqft):'))
            no_of_floors = int(input('Enter the number of floors the building has :'))
            office_space_area = int(input('Enter the office space area the building has :'))
            rent_per_squarefoot = int(input('Enter rent per squarefoot of the building :'))

            building = CommercialBuilding(address,no_of_floors,total_area,office_space_area,rent_per_squarefoot)
            Building.buildings[building.SR_NO] = building

            if not building :
                print('Registration is Failed.')
        
        elif choice == 3 :
            print('Gathering the List of all Properties...')
            building = Building.buildings
            for i in building :
                print(building[i])
        
        elif choice == 4:
            print('Exiting the Building Info Dashboard..')
            print('Thank You.')
            break