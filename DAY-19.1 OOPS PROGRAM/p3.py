# Create a Python class called ElectronicsProduct with
# attributes for product ID, name, and price. Include
# methods to apply discount and calculate final price.
# Create a subclass called WashingMachine that adds a
# warranty period attribute and includes a method to
# extend the warranty period.

class ElectronicProduct :

    checkout_items = {}
    products = {}
    product_id = 0
    def __init__(self,product_name,price):
        self.PRODUCTS = ElectronicProduct.products
        self.CHECKOUT_ITEMS = ElectronicProduct.checkout_items
        ElectronicProduct.product_id += 1
        self.PRODUCT_ID = ElectronicProduct.product_id
        self.PRODUCT_NAME = product_name
        self.PRICE = price
    
    def __str__(self):
        return f"ID :{self.PRODUCT_ID} | {self.PRODUCT_NAME} | :₹{self.PRICE}"
    
    def discount(self,discount_choice,total_price):
            if(discount_choice == 'Y') or (discount_choice == 'y') :
                discount_value=int(input('How much discount to apply (not to use \'%\')? ->'))
                discount_amount = total_price * (discount_value/100)
                total_price -= discount_amount
                return total_price
            elif (discount_choice == 'N') or (discount_choice == 'n') :
                return total_price
            else:
                print('Invalid Choice.Please enter a valid option.')
                return total_price
 
    def checkout(self):
        checkout_items = ElectronicProduct.checkout_items
        final_amount = 0
        print('======================')
        print('Checkout Bill :')
        for product in checkout_items :
            item = checkout_items.get(product)
            print(item)
            final_amount += item.PRICE
        print('======================')    
        discount_choice=input('Do you want to use discount coupons :\'Y\' for Yes and \'N\' for No :')
        final_amount = self.discount(self,discount_choice,final_amount)
        print('Total amount :',final_amount)    
        return final_amount

   
        

class WashingMachine(ElectronicProduct):
    def __init__(self, product , price, warranty_period):
        super().__init__(product,price)
        self.WARRANTY_PERIOD = warranty_period
    
    def __str__(self):
        return super().__str__()+f" |warranty_period :{self.WARRANTY_PERIOD}"  
    
    def register_product(self,product_name,price,warranty_period):        
        product = WashingMachine(product_name,price,warranty_period)
        ElectronicProduct.products[product.PRODUCT_ID] = product
        if ElectronicProduct.products :
            return True
        return False
    
    def extention_warranty_period(self,product_id,time_period):
        product = ElectronicProduct.products.get(product_id)
        if not product:
            print('Product not found.')
        product.WARRANTY_PERIOD += time_period
        return product.WARRANTY_PERIOD
    
    def billing_system(self):
        products = ElectronicProduct.products
        checkout_items = ElectronicProduct.checkout_items
        if not products:
            print('Sorry, We are out of stock.')
            return False
        
        while True:
            print('\nWecome to the Billing System !')
            print('Please choose from the available products :')
            counter = 1
            for item in products:
                product = products.get(item)
                print(f'{counter}|{product}')
                counter += 1
            print(f'{counter}.Exit')
            print('============================================')
            choice = int(input('Enter the product ID here :'))
            checkout_items[choice] = products.get(choice)
            billing_choice = input('Do you want to add another product : \'Y\' for Yes and \'N\' for No :')
            if (billing_choice == 'Y') or (billing_choice == 'y') :
                continue
            elif (billing_choice == 'N') or (billing_choice == 'n') :
                warranty_extension_choice = input('Do you want to extend warranty period :\'Y\' for Yes and \'N\' for No :')
                if(warranty_extension_choice == 'Y') or (warranty_extension_choice == 'y') :
                    time_period = int(input('Warranty Time Period Extension (in yrs) :'))
                    self.extention_warranty_period(self,choice,time_period)
                if not checkout_items:
                    print('No items to checkout!!')
                    break
                print(ElectronicProduct.checkout(ElectronicProduct))
                break

            else :
                print('Invalid Choice.Please enter a valid option.')
    
    # def display(self):
    #     print('Checkout bill for' ,self.PRODUCT_ID ,self.PRODUCT_NAME,'is',self.PRICE,'with warranty of',self.WARRANTY_PERIOD,'years.')

# product1 = WashingMachine(1,"LG",25000,2)
# product1.discount(20)
# product1.extention_warranty_period()
# product1.display()

class main(WashingMachine):
    while True:
        print('\n=====================================')
        print('Welcome to Electronic Porduct Market !')
        print('Please choose the options given below :')
        print('1.Register a Product')
        print('2.Billing Process')
        print('3.Exit')
        print('======================================')
        
        choice = int(input('Enter your choice here :'))

        if choice == 1 :
            print('Entering the Registration Dashboard...')
            product_name = input('Enter the name of the product :')
            price = int(input('Enter the price of the product in numbers :'))
            warrranty_period = int(input('Enter the default Warranty periods (in yrs) :'))
            product = WashingMachine.register_product(WashingMachine,product_name,price,warrranty_period)
            if product :
                print('Product Registration is successful.!')
            else :
                print('Product Registration is failed.!')
        elif choice == 2:
            print('entering Billing Dashboard :')
            WashingMachine.billing_system(WashingMachine)
        elif choice == 3:
            print('\nExiting Electronic Product Market Dashboard.')
            print('Thank You and Visit again.')
            break
        else :
            print('Invalid Choice.Please enter a valid option.')
