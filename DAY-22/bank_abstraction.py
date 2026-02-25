# . Create a Python class called BankAccount with attributes
# for account number, account holder name, and balance.
# Include methods to deposit money, withdraw money, and
# check current balance.Create a subclass called
# SavingsAccount that adds an interest rate attribute and
# includes a method to apply interest to the balance.

from abc import ABC,abstractmethod
class BankAccount(ABC) :
    
    accounts = {}
    
    def __init__(self , account_number,account_name,balance):
        self.ACCOUNT_NUMBER = account_number
        self.ACCOUNT_NAME = account_name
        self.BALANCE = balance
    
    def create_account(self,account_number,account_name , balance):
        account = BankAccount(account_number,account_name,balance)
        self.accounts[account_number] = account
    
    @abstractmethod
    def deposit():
        pass
    @abstractmethod
    def withdraw():
        pass
    
    def check_balance(self ,account_number ):
        account = self.accounts.get(account_number)
        if not account:
            print('Account not found.')
            return False
        print('The balance is :', account.BALANCE)


# s1 = BankAccount(1,'mal',4500)
# s1.deposit(1200)
# s1.withdraw(1500)
# s1.check_balance()

class SavingsAccount(BankAccount):
    interestRate = 6.5
    interest = 0 

    @staticmethod
    def deposit(self, account_number,deposit_value):
        account = self.accounts.get(account_number)
        if not account :
            print('Account not found')
            return False
        if deposit_value <= 0 :
            print('Enter the positive number.')
            return False
        account.BALANCE += deposit_value
        return account.BALANCE
    
    @staticmethod
    def withdraw(self,account_number,withdraw_amount):
        account = self.accounts.get(account_number)
        if not account:
            print('Account not found.')
            return False
        if account.BALANCE < withdraw_amount:
            print('Balance is not enough.')
            return False
        account.BALANCE -= withdraw_amount
        return account.BALANCE
    
    def interest_provision(self ,account_number, time):
        account = self.accounts.get(account_number)
        if not account:
            print('Account not found.')
            return False
        interest = account.BALANCE*self.interestRate*time
        account.BALANCE += interest
        return account.BALANCE

class CurrentAccount(BankAccount):
    interestRate = 7.5
    interest = 0 

    @staticmethod
    def deposit(self, account_number,deposit_value):
        account = self.accounts.get(account_number)
        if not account :
            print('Account not found')
            return False
        if deposit_value <= 0 :
            print('Enter the positive number.')
            return False
        account.BALANCE += deposit_value
        return account.BALANCE
    
    @staticmethod
    def withdraw(self,account_number,withdraw_amount):
        account = self.accounts.get(account_number)
        if not account:
            print('Account not found.')
            return False
        if account.BALANCE < withdraw_amount:
            print('Balance is not enough.')
            return False
        account.BALANCE -= withdraw_amount
        return account.BALANCE
    
    def interest_provision(self ,account_number, time):
        account = self.accounts.get(account_number)
        if not account:
            print('Account not found.')
            return False
        interest = account.BALANCE*self.interestRate*time
        account.BALANCE += interest
        return account.BALANCE
    
class dashboard(SavingsAccount,CurrentAccount):
    
    while True:
        print('\n===========================================')
        print('Welcome to MBH bank CLI:')
        print('Please choose the Options provided below :')
        print('1.Create/Register Account.')
        print('2.Deposit Amount.')
        print('3.Withdraw Amount')
        print('4.Adding Interest.')
        print('5.Checking the balance.')
        print('6.Exit.')
        print('===========================================\n')
        choice = input('Enter the choice here ->')
        
        if choice == '1' :
            print('Entering Registration System :')
            account_number=int(input('Enter the account number :'))
            account_holder_name = input('Enter the account holder name :')
            balance = int(input('Enter the amount you are currently having :'))

            super().create_account(account_number,account_holder_name,balance)
            print('Account is successfully registered.')
        
        elif choice == '2' :
            print('Entering Deposit Dashboard :')
            account_number = int(input('Enter the account number here ->'))
            deposit_amount = int(input('Enter the deposit amount here ->'))
            balance = super().deposit(account_number,deposit_amount)
            print('Current Balance :' , balance)
        
        elif choice == '3' :
            print('Entering Withdrawal Dashboard :')
            account_number = int(input('Enter the account number here ->'))
            withdrawal_amount = int(input('Enter the withdrawal amount here ->'))
            balance = super().withdraw(account_number,withdrawal_amount)
            print('Current Balance :' , balance)
        
        elif choice == '4':
            print('Entering Savings Account Dashboard :')
            account_number = int(input('Enter the account number here ->'))
            time_period = int(input('Enter the time period here ->'))
            balance = super().interest_provision(account_number,time_period)
            print('Current Balance :' , balance)
        
        elif choice == '5' :
            account_number = int(input('Enter the account number :'))
            print('Checking Your Balance :')
            super().check_balance(account_number)
        
        elif choice == '6' :
            print('Exiting the System.')
            print ('Thank You.')
            break
        
        else :
            print('Please enter a valid choice.')
