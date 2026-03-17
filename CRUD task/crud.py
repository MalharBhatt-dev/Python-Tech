import sqlite3
from datetime import date

#~ -------------------Insert Data-----------------
Manager = {"SALES": "Mr Rohit", "IT": "Mr Shyam", "HR": "Mr Raj"}

def insert_data(obj):

    insert_main_employee(obj)

    insert_department_employee(obj)

    search_employee(obj.EMPID)


def insert_department_employee(obj):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()
    cursor.execute(f"INSERT INTO {obj.DEPARTMENT} VALUES(?,?,?,?,?,?,?)", (obj.EMPID,obj.ENAME, obj.DEPARTMENT, obj.MOBNUMBER, obj.SALARY, obj.JD, obj.Manager  ))
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
    cursor.execute(f"select department from employee where empid = {empid}")
    record = cursor.fetchone()
    cursor.execute(f"DELETE FROM EMPLOYEE WHERE EMPID = {empid}")
    cursor.execute(f"delete from {record[0]} where empid = {empid}")
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

#~ -----------------------Change Departments----------------

def change_department(empid , new_dept):
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()
    # cursor.execute(f"select * from employee where empid = {empid}") #!SQL Injection May occur using this format.
    cursor.execute(f"select * from employee where empid = ?",(empid,))
    record = cursor.fetchone()
    cursor.execute('update employee set department = ? where empid = ?',(new_dept,empid))
    cursor.execute(f"select * from employee where empid = ?",(empid,))
    new_record = list(cursor.fetchone())
    new_record.append(Manager[new_dept])
    print(new_record)
    cursor.execute(f"INSERT INTO {new_dept} (EMPID , ENAME,DEPARTMENT,MOBILENUMBER,SALARY,JD,MANAGER) VALUES (?,?,?,?,?,?,?)",(tuple(new_record)))
    cursor.execute(f"select * from {new_dept} where empid = ?",(empid,))
    dept_record = cursor.fetchone()
    print(dept_record)
    cursor.execute(f'delete from {record[2]} where empid = ?',(empid,))
    print("Updation is successful.")
    data.commit()
    data.close()

# *--------------------Login-----------------


# def login():

#     password = input("Enter Password: ")
#     if password == '1234':
#         print("Login Successful")
#     else:
#         print("Login Failed")


# login()