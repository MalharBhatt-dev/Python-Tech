# Create a Python class called ElectronicsProduct with
# attributes for product ID, name, and price. Include
# methods to apply discount and calculate final price.
# Create a subclass called WashingMachine that adds a
# warranty period attribute and includes a method to
# extend the warranty period.

class ElectronicProduct :
    checkout = {}
    products = {}
    def __init__(self,product_id,product_name,price):
        self.PRODUCT_ID = product_id
        self.PRODUCT_NAME = product_name
        self.PRICE = price

    def discount(self,discount_value):
        # product = self.products.get(product_id)
        discount_amount = self.PRICE * (discount_value/100)
        self.PRICE -= discount_amount
        print('The Final Price of the Product after discount is :',self.PRICE)
    

class WashingMachine(ElectronicProduct):
    def __init__(self ,product_id, product , price, warranty_period):
        super().__init__(product_id,product,price)
        self.WARRANTY_PERIOD = warranty_period
    
    def extention_warranty_period(self):
        self.WARRANTY_PERIOD += 1
        print('The warranty is now extended to :',self.WARRANTY_PERIOD)
    
    def display(self):
        print('Checkout bill for' ,self.PRODUCT_ID ,self.PRODUCT_NAME,'is',self.PRICE,'with warranty of',self.WARRANTY_PERIOD,'years.')

product1 = WashingMachine(1,"LG",25000,2)
product1.discount(20)
product1.extention_warranty_period()
product1.display()


            