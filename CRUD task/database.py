import sqlite3
from datetime import date


def table_creation():
    data = sqlite3.connect('TESTYANTRA.db')
    cursor = data.cursor()

    # * --------------MAIN EMPLOYEE TABLE-----------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS EMPLOYEE(EMPID INTEGER PRIMARY KEY AUTOINCREMENT , ENAME TEXT, DEPARTMENT TEXT, MOBILENUMBER BIGINT, SALARY INTEGER, JD TEXT)
    ''')

    # * --------------SALES DEPARTMENT-----------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SALES( EMPID INTEGER, ENAME TEXT, DEPARTMENT TEXT, MOBILENUMBER BIGINT, SALARY INTEGER, JD TEXT,MANAGER TEXT)
    ''')

    # * --------------HR DEPARTMENT--------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HR( EMPID INTEGER, ENAME TEXT, DEPARTMENT TEXT, MOBILENUMBER BIGINT, SALARY INTEGER, JD TEXT, MANAGER TEXT)
    ''')

    # * --------------IT DEPARTMENT--------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS IT( EMPID INTEGER, ENAME TEXT, DEPARTMENT TEXT, MOBILENUMBER BIGINT, SALARY INTEGER, JD TEXT, MANAGER TEXT)
    ''')

    data.commit()
    data.close()


table_creation()