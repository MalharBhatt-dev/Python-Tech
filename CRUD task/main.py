from database import *
from crud import *
# * -------------------Class-----------------
class Bank:
    
    Location = 'Navrangpura'

    def __init__(self, ename, department, mobnumber, salary):

        self.ENAME = ename
        self.DEPARTMENT = department
        self.MOBNUMBER = mobnumber
        self.JD = date.today().isoformat()
        self.SALARY = salary
        self.Manager = Manager[department]

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
    6 Delete Employee
    7 Department Employees
    8 Exit
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
        new_dept = input("Enter New Department name: ")
        change_department(empid, new_dept)
    elif choice == 6:
        empid = int(input("Enter EMPID: "))
        delete_employee(empid)
    elif choice == 7:
        dept = input("Enter Department: ")
        department_employee(dept)
    elif choice == 8:
        print("Exiting...")
        break