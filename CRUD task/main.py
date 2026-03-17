from database import *
from crud import *
# * -------------------Class-----------------
class Bank:
    Location = 'Navrangpura'
    Manager = {'Sales': "Mr Rohit", "IT": "Mr Shyam", "HR": "Mr Raj"}

    def init(self, ename, department, mobnumber, salary):

        self.ENAME = ename
        self.DEPARTMENT = department
        self.MOBNUMBER = mobnumber
        self.JD = date.today().isoformat()
        self.SALARY = salary
        self.Manager = Bank.Manager[department]

        insert_data(self)

        print('DATA INSERTED SUCCESSFULLY')


    # * -------------------Menu-----------------

    while True:
        print("""
        1 Add Employee
        2 Display Employees
        3 Search Employee
        4 Update Salary
        5 Change Department
        5 Delete Employee
        6 Department Employees
        7 Exit
        """)

        choice = int(input("Enter Choice: "))

        if choice == 1:
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            mob = int(input("Enter Mobile: "))
            sal = int(input("Enter Salary: "))
            Bank(name, dept, mob, sal)

        elif choice == 2:
            display_all()

        elif choice == 3:
            empid = int(input("Enter EMPID: "))
            search_employee(empid)

        elif choice == 4:
            empid = int(input("Enter EMPID: "))
            sal = int(input("Enter New Salary: "))
            update_salary(empid, sal)

        elif choice == 5:
            empid = int(input("Enter EMPID: "))
            delete_employee(empid)

        elif choice == 6:
            dept = input("Enter Department: ")
            department_employee(dept)

        elif choice == 7:
            print("Exiting...")
            break