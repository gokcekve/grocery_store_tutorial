import mysql.connector
import datetime

__cnx = None

def get_sql_connection():
    print("Opening MySQL Connection")  # mysql workbench
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='3534', host='localhost', database='grocery_store')

    return __cnx