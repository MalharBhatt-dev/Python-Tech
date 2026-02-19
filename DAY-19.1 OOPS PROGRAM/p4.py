
#h Create a Python class called Building with attributes for
#h address, number of floors, and total area. Create two
#h subclasses: ResidentialBuilding (adds number of
#h apartments and rent per apartment) and
#h CommercialBuilding (adds office space area and rent per
#h square foot). Each subclass should include a method to
#h calculate total rent

class Building :
    
    def __init__(self,address,noOfFloors,totalArea):
        self.ADDRESS = address
        self.NO_OF_FLOORS = noOfFloors
        self.TOTAL_AREA = totalArea

class ResidentialBuilding(Building):
     def __init__(self,address,no_of_floors,total_area,no_of_apartments,rent_per_apartment):
        super().__init__(address,no_of_floors,total_area)
        self.NO_OF_APARTMENTS = no_of_apartments
        self.RENT_PER_APARTMENT = rent_per_apartment
     
     def calculate_rent(self):
         rent_amt =  self.NO_OF_APARTMENTS * self.NO_OF_FLOORS*self.RENT_PER_APARTMENT 
         return rent_amt

     
     def display(self):
         print('\nThe rent of Residential Building at',self.ADDRESS,'\nhaving',self.NO_OF_FLOORS,'\nwith total area',self.TOTAL_AREA,'sqft \nhaving',self.NO_OF_APARTMENTS,'number of apartments and\nhaving rent per apartment as',self.RENT_PER_APARTMENT,'is ₹',self.calculate_rent(),'\n')         

class CommercialBuilding(Building):
     def __init__(self,address,no_of_floors,total_area,office_space_area,rent_per_square_foot):
        super().__init__(address,no_of_floors,total_area)
        self.OFFICE_SPACE_AREA = office_space_area
        self.RENT_PER_SQUARE_FOOT = rent_per_square_foot
     
     def calculate_rent(self):
         rent_amt = self.OFFICE_SPACE_AREA*self.RENT_PER_SQUARE_FOOT*self.NO_OF_FLOORS
         return rent_amt
     
     def display(self):
         print('\nThe rent of Commercial Building at',self.ADDRESS,'\nhaving',self.NO_OF_FLOORS,'\nwith total area',self.TOTAL_AREA,'sqft \nhaving office space area as',self.OFFICE_SPACE_AREA,'sqft and\nhaving rent per square foot as',self.RENT_PER_SQUARE_FOOT,'sqft is ₹',self.calculate_rent(),'\n')

r1 = ResidentialBuilding("abc",3,2500,6,4500)
r1.display()

r2 = CommercialBuilding('def',5,2000,202,1200)
r2.display()