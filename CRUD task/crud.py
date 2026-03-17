import sqlite3
from datetime import date

#* -------------------Insert Data-----------------

def insert_data(obj):
    departments = ['HR', 'SALES', 'IT']

    insert_main_employee(obj)

    insert_department_employee(obj, departments)

    search_employee(obj.EMPID)


def insert_department_employee(obj, departments):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    if obj.DEPARTMENT in departments:
        table_name = obj.DEPARTMENT.upper()

        cursor.execute(f"INSERT INTO {table_name} VALUES(?,?,?,?,?,?,?)", (obj.EMPID,
            obj.ENAME, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD, obj.Manager  ))

    else:
        print("INVALID DEPARTMENT")

    data.commit()
    data.close()


def insert_main_employee(obj):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute(
        "INSERT INTO EMPLOYEE(ENAME,DEPARTMENT,MOBILENUMBER,SALARY,JD) VALUES(?,?,?,?,?)",
        (obj.ENAME, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD)
    )

    obj.EMPID = cursor.lastrowid

    data.commit()
    data.close()
    return obj.EMPID

# * -------------------Display Data-----------------

def display_all():
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute("SELECT * FROM EMPLOYEE")
    records = cursor.fetchall()

    for i in records:
        print(i)

    data.close()


# * -------------------Search Employee-----------------

def search_employee(empid):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute("SELECT * FROM EMPLOYEE WHERE EMPID=?", (empid,))
    record = cursor.fetchone()

    if record:
        print(record)
    else:
        print("Employee Not Found")

    data.close()


# * -------------------Update Salary-----------------

def update_salary(empid, new_salary):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute("UPDATE EMPLOYEE SET SALARY=? WHERE EMPID=?",
                   (new_salary, empid))

    data.commit()
    data.close()

    print("Salary Updated Successfully")


# * -------------------Delete Employee-----------------

def delete_employee(empid):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute("DELETE FROM EMPLOYEE WHERE EMPID=?", (empid,))

    data.commit()
    data.close()

    print("Employee Deleted Successfully")


# * -------------------Department Employees-----------------

def department_employee(dept):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    cursor.execute(f"SELECT * FROM {dept}")
    records = cursor.fetchall()

    for i in records:
        print(i)

    data.close()


# *--------------------Login-----------------


# def login():

#     password = input("Enter Password: ")
#     if password == '1234':
#         print("Login Successful")
#     else:
#         print("Login Failed")


# login()